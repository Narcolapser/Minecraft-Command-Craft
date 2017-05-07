# Minecraft-Command-Craft
A set of scripts for converting blender models into single command constructions in minecraft.

# Explanation of scripts

## Command Joiner
Takes a list of commands and joins them into a single tower. It can be run as a script, but know that it does not modify the commands in any way. You will have to deal with the offset yourself before hand.

## Command Relativizer
This script will take a command that uses absolute coordinates and translate them into relative coordinates with an offset specified. In this way you can prepare a list of commands to be joined by command Joiner.

## mcpile
This takes a list of absolute commands and runs them through command Relativizer and Command Joiner. Thus turning a list of raw, absolute commands into a list a single command.

## objtofill
This script takes an obj file, such as one exported from blender, and turns it into a list of fill commands. This is a dumb script, it makes a bounding box out of the points you give to determine the fill size, rounding as it goes. It does no logic to figure out the best way to do the fills, that's your job in blender. 

# Basic order of things
Build an object in blender. You will make a bounding box for every fill command. So each fill is a different object, that's important. Export that object from blender to an obj. Run objtofill.py on it. save the out put to a file. Run mcpile on that. Save the output to your clip board, paste into a minecraft command block.


