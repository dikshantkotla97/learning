def volume(height, depth, width):
    height_given = int(height)
    depth_given = int(depth)
    width_given = int(width)
    result = height_given * depth_given * width_given
    return result

print("For volume calculation please enter values:")
height_input = input("Height: ")
depth_input = input("Depth: ")
width_input = input("Width: ")
volume_result = volume(height_input, depth_input, width_input)
print("The volume is: " + str(volume_result))
