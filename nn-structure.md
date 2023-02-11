# Neuronal network structure

## Features and labels

Features: Random normalized integers

Labels:

1. Vector3(r,g,b) int - Background (Min: 0, Max: 255)
2. Vector3(r,g,b) int - Foreground (Min: 0, Max: 255)
3. Int - FontSize (Min: 6, Max: 24)
4. Bool (0,1) int - FocusVisualStyle (Min: 0, Max: 1)
5. Vector3(r,g,b) int - BorderBrush (Min: 0, Max: 255)
6. Int - BorderThickness (Min: 1, Max: 12)
7. Bool (0,1) int - Button.IsFocused (Min: 0, Max: 1)
8. Int - BorderThickness (Button.IsFocused) (Min: 1, Max: 12)
9. Vector3(r,g,b) int - BorderBrush (Button.IsFocused) (Min: 0, Max: 255)
10. Bool (0,1) int - Button.IsEnabled (Min: 0, Max: 1)
11. Vector3(r,g,b) int - Background (Button.IsEnabled) (Min: 0, Max: 255)
12. Vector3(r,g,b) int - BorderBrush (Button.IsEnabled) (Min: 0, Max: 255)
13. Bool (0,1) int - Rounding (Min: 0, Max: 1)
14. Int - CornerRadius (Rounding) (Min: 2, Max: 16)
15. Bool (0,1) int - Button.MouseEnter (Min: 0, Max: 1)
16. Vector3(r,g,b) int - To (Button.MouseEnter)  (Min: 0, Max: 255)
17. Float (2 two numbers before the decimal point) - Duration (seconds - Button.MouseEnter) (Min: 0.20, Max: 1.5)
18. Bool (0,1)  int - Button.MouseLeave (Min: 0, Max: 1)
19. Vector3(r,g,b) int - To (Button.MouseLeave) (Min: 0, Max: 255)
20. Float (2 two numbers before the decimal point) - Duration (seconds - Button.MouseLeave) (Min: 0.20, Max: 1.5)
