# RE Pipeline | Project Manager

Basic pipeline (more like smart project folder structure) for small vfx projects.
Idea for this one is that it is very hard to come up with project folder structure that works for multiple applications. 
Usually you end up with a huge mess - files from different apps mixed together and hard to use relative paths (../../../scene/textures/bricks.jpg).
Another issue is when it comes time to clean things up for archiving - everything is mixed together. It's hard to know which files, sequences and temporary files are safe to remove (that can be easily re-generated if you need to work on the project in the future). 

I try to solve all of these issues with clever use of symlinks. It's a feature that is common in Linux/Unix/Mac based systems, where you can create "virtual" folders - folders that actually point to other folders that are located elswhere. This allows building paths relative to these virtual folders and not actual target folders. 

To use symlinks on Windows, you must have NTFS filesystem and enable developer mode in windows settings (Update & Security -> For developers -> Developer Mode : ON)

To simplify everything, I assume the following workflow:
1. You build Assets (Props, Characters, Environments etc.) and export (publish) final usable results (fbx, usd, abc, blend etc.) files in shared assets folder. 
2. You link or import thse finished assets into your shots or other assets scenes from shared folder. 

Each asset or shot, has a bunch of symlink folders in local Shot or Asset folder pointing to shared asset folders. 

Here is project structure explained in more detail: 

ProjectRoot
	
	Assets [Assets shared between shots and apps] Don't use directly!
		2D
			Artworks
		3D
			Fbx
			Bgeo
			Obj
			Alembic
			USD
			C4D
			Blend
		Tex
			Ext [link to External texture lib]
		Lib
			Python_Libs
	
	Build [ Buildig assets, scenes, etc. ]
		Asset_Name_A
			[Houdini]
				Link: Assets/Tex
				Link: Fbx,Bgeo,Obj,Alembic,USD
				Link: Render
				Link: Temp/Tmp_Shared
			[Blender]
				Link: Assets/Tex
				Link: Fbx,Obj,Alembic,USD
			[C4D]
				Link: Assets/Tex
				Link: Fbx,Obj,Alembic,USD
			[Textures]
				Link: Shared/Tex
        Asset_Name_B
            ...
	Shots
		Shot_XYY [Versions are inside folders using filenames]
			Blend
				Link: Assets_fbx, obj, bgeo, alembic, Tex..
			Houdini
				Link: Assets_fbx, obj, bgeo, alembic, Tex..
				Link: Temp/ShotX
				Link: Temp/Shared
			[Maya]
			[C4D]
			Comp [References sequences from Render]
				Link: Shared/2D/Artworks (Images needed for compositing)
				Link: Render/Shots/Shot_XYY
				Link: Render/Previs/Shot_XYY
				Link: Out (Project main output folder (deliver, images, previs, review)
	
	Render [Rendered Image sequences. Can remove when archiving to save space]
		Assets
			Asset_Name
		Previs
			Shot_SEQXX_vXX
		Shots
			Shot_SEQXX_vXX
		
	
	Out [Valuable project outputs]
		Previs [all previs videos]
		Review [all "final" videos]
		Images [stills, screenshots, making of pics etc]
		Deliver - place for final deliveries
		
	
	Temp [ Folder to remove when archiving or saving space ]
		Assets
			Asset_Name
				Flip
				Geo
				Sim
		Shots
			Shot_XYY
				Flip
				Geo
				Sim
				
	Other potential folders:

	Comp [Global project comp folder]
		Link: Shared/2D/Artworks (Images needed for compositing)
		Link: Render/Shots/
		Link: Render/Previs/
        Link: Out (Project main output folder (deliver, images, previs, review)

