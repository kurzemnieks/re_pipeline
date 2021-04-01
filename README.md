# RE Pipeline | Project Manager

Basic pipeline (more like smart project folder structure) for small vfx projects.
Idea for this one is that it is very hard to come up with project folder structure that works for multiple applications. 
Usually you end up with a huge mess - files from different apps mixed together and hard to use relative paths (../../../scene/textures/bricks.jpg).
Another issue is when it comes time to clean things up for archiving - everything is mixed together. It's hard to know which files, sequences and temporary files are safe to remove (that can be easily re-generated if you need to work on the project in the future). 

I try to solve all of these issues with clever use of symlinks. It's a feature that is common in Linux/Unix/Mac based systems, where you can create "virtual" folders - folders that actually point to other folders that are located elswhere. This allows building paths relative to these virtual folders and not actual target folders. 
