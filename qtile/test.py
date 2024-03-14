import os

def parse_colors_sh(file_path):
    colors = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith("color"):
                parts = line.strip().split("=")
                if len(parts) == 2:
                    color_value = parts[1].strip().strip('"')
                    colors.append(color_value)
    return colors

colors_sh_path = '~/.cache/wal/colors.sh'  # Path to colors.sh
expanded_colors_sh_path = os.path.expanduser(colors_sh_path)  # Expanding ~ to full path
if os.path.exists(expanded_colors_sh_path):
    colors = parse_colors_sh(expanded_colors_sh_path)

    # Print the colors
    for color_value in colors:
        print(color_value)
else:
    print("The specified path does not exist.")

