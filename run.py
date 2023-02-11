import inputgen
import log
import model as nn
import cupy as np
import uuid
import sys

# How to use: run.py <model file>

# Getting all arguments from terminal
argv = sys.argv

def rgb_to_hex(r, g, b):
    """Convert an RGB color tuple to a hexadecimal string"""
    # Convert the values to integers
    r, g, b = int(r), int(g), int(b)
    # Clamp the values to the range 0-255
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    # Convert the values to hexadecimal strings
    hex_r = hex(r)[2:].zfill(2)
    hex_g = hex(g)[2:].zfill(2)
    hex_b = hex(b)[2:].zfill(2)
    # Concatenate the hex strings into a single hexadecimal string
    return f"#{hex_r}{hex_g}{hex_b}"

log.info("Starting XAML-STYLEGEN")

if not len(argv) > 1:
    log.error("The first required argument is missing: the name of the model file without extension in the models folder")
    sys.exit(1)
else:
    model = nn.load_model(f"models\\{argv[1]}.h5")
    log.info(f"Loaded model {argv[1]}.h5")

rng = int(input("How many styles you need to generate: "))
log.info("Generating xml style files")
for i in range(rng):
    x = inputgen.generate_inputs(nn.get_batch_size()).get()
    indices = np.arange(x.shape[0])
    np.random.shuffle(indices)
    x = x[indices.get()]
    
    predictions = model.predict(x)

    np.set_printoptions(suppress=True, precision=2)
    predictions_res = np.round(predictions, decimals=2)
    predictions_res = np.fabs(predictions_res).get()

    isfocused = f"""<Trigger Property="Button.IsFocused" Value="True">
    <Setter TargetName="border" Property="BorderThickness" Value="{int(predictions_res[0][13])}" />
        <Setter TargetName="border" Property="BorderBrush" Value="{rgb_to_hex(int(predictions_res[0][14]), int(predictions_res[0][15]), int(predictions_res[0][16]))}" />
    </Trigger>"""

    isenabled = f"""<Trigger Property="Button.IsEnabled" Value="False">
    <Setter Property="Background" Value="{rgb_to_hex(int(predictions_res[0][18]), int(predictions_res[0][19]), int(predictions_res[0][20]))}" />
        <Setter TargetName="border" Property="BorderBrush" Value="{rgb_to_hex(int(predictions_res[0][21]), int(predictions_res[0][22]), int(predictions_res[0][23]))}" />
    </Trigger>"""

    rounding = f"""<Style.Resources>
        <Style TargetType="Border">
            <Setter Property="CornerRadius" Value="{int(predictions_res[0][25])}" />
        </Style>
    </Style.Resources>"""

    mouseentered = f"""<EventTrigger RoutedEvent="Button.MouseEnter">
            <EventTrigger.Actions>
                <BeginStoryboard>
                    <Storyboard>
                        <ColorAnimation
                        Storyboard.TargetProperty="(Button.Background).(SolidColorBrush.Color)"
                        To="{rgb_to_hex(int(predictions_res[0][27]), int(predictions_res[0][28]), int(predictions_res[0][29]))}" Duration="0:0:{float(predictions_res[0][30])}" />
                    </Storyboard>
                </BeginStoryboard>
            </EventTrigger.Actions>
    </EventTrigger>"""

    mouseleave = f"""<EventTrigger RoutedEvent="Button.MouseLeave">
            <EventTrigger.Actions>
                <BeginStoryboard>
                        <Storyboard>
                            <ColorAnimation
                            Storyboard.TargetProperty="(Button.Background).(SolidColorBrush.Color)"
                            To="{rgb_to_hex(int(predictions_res[0][32]), int(predictions_res[0][33]), int(predictions_res[0][34]))}" Duration="0:0:{float(predictions_res[0][35])}" />
                        </Storyboard>
                </BeginStoryboard>
            </EventTrigger.Actions>
    </EventTrigger>"""

    with open(f'outputs\\{str(uuid.uuid4())}.xml', 'w') as xml:
        xml.write(
        f'''<Style x:Key="CustomButtonStyle" TargetType="Button">
        <Setter Property="Background" Value="{rgb_to_hex(int(predictions_res[0][0]), int(predictions_res[0][1]), int(predictions_res[0][2]))}" />
        <Setter Property="Foreground" Value="{rgb_to_hex(int(predictions_res[0][3]), int(predictions_res[0][4]), int(predictions_res[0][5]))}" />
        <Setter Property="FontSize" Value="{int(predictions_res[0][6])}" />
        {'<Setter Property="FocusVisualStyle" Value="{{x:Null}}" />' if int(predictions_res[0][7]) == 1 else ''}
        <Setter Property="VerticalContentAlignment" Value="Center" />
        <Setter Property="HorizontalContentAlignment" Value="Center" />
        <Setter Property="Template">
            <Setter.Value>
                <ControlTemplate TargetType="{{x:Type Button}}">
                    <Border Background="{{TemplateBinding Background}}" Cursor="Hand">
                        <Border x:Name="border" BorderBrush="{rgb_to_hex(int(predictions_res[0][8]), int(predictions_res[0][9]), int(predictions_res[0][10]))}" BorderThickness="{int(predictions_res[0][11])}" Background="Transparent">
                            <ContentPresenter VerticalAlignment="{{TemplateBinding VerticalContentAlignment}}" HorizontalAlignment="{{TemplateBinding HorizontalContentAlignment}}" ContentSource="{{TemplateBinding Content}}" />
                        </Border>
                    </Border>
                    <ControlTemplate.Triggers>
                        {isfocused if int(predictions_res[0][12]) == 1 else ''}
                        {isenabled if int(predictions_res[0][17]) == 1 else ''}
                    </ControlTemplate.Triggers>
                </ControlTemplate>
            </Setter.Value>
        </Setter>
        
        {rounding if int(predictions_res[0][24]) == 1 else ''}

        <Style.Triggers>
            {mouseentered if int(predictions_res[0][26]) == 1 else ''}

            {mouseleave if int(predictions_res[0][31]) == 1 else ''}
        </Style.Triggers>
    </Style>
    ''')