# ManimRepl

This is a sample Repl to show how `manim` can be run on [repl.it](https://repl.it) with minimum frustration.

# How To Use:

1. Write the code your animation needs in `main.py`, or any other python file.
2. Then, go to the shell, and run the command to render your animation.
  For example :
    `python3 -m manim main.py -ql`
  Don't use the `-p` tag, and read the `Limitations` section for info on why.

## Addons Required:
The only addon needed to run fully-featured (well, mostly) `manim` on `repl.it` is [manim-onlinetex](https://github.com/ManimCommunity/manim-onlinetex). 
repl.it doesn't come with `LaTeX` pre-installed, and you can't really fit the required packages into the 500mb that `repl.it`'s free tier provides, so we have to outsource `LaTeX` rendering to other online services, which is what `manim-onlinetex` does.
Of course, if you don't use objects that need `LaTeX` (`Tex` and `MathTex` are some examples), you can get away with not installing `manim-onlinetex`.

If you're using `manim-onlinetex`, then avoid clearing the `Tex` directory of your media directory. This is so you don't contact the external LaTeX rendering APIs too often and put an unnecessary strain on their servers.

## Limitations:
Don't render your animations with the `-p` tag. It completely messes with `repl.it`'s output display tab as it struggles to find a program that can open multimedia files. Instead, you'll have to manually click through to your video/image file via the sidebar's `Files` tab and open it that way.

If you're using `manim-onlinetex`, then try not to clear the `Tex` directory of your media directory so you don't strain the external APIs by contacting them too frequently.