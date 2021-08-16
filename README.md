# TurtleBot

A Turtle scripting bot for Discord. Give it a script from the quick language below, and it will draw and send an image of the result.

## Syntax:
Commands, or single letters, are given to the bot, followed by a number. The number could be a number of pixels, degrees, or a 1 or 0 for true and false.
Each command is seperated by a comma.

Here's a quick example, for drawing a 100x100 square:
```
F100,R90,F100,R90,F100,R90,F100,R90
```

### Commands:
- `F<n>`: Move the pointer forward `n` pixels.
- `B<n>`: Move the pointer backwords `n` pixels.
- `L<n>`: Turn the poniter left `n` degrees.
- `R<n>`: Turn the pointer right `n` degrees.
- `A<n>`: Set the angle of the pointer.
- `P<n>`: Set the pen state. `n` can be `0` for off, `1` for on.

## Discord commands:
The following are slash commands:
- `/help`: Show a message similar to the **Syntax** section above, detailing how to use the bot
- `/draw <code>`: The command to run your script.