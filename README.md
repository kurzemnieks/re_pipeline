# RE Pipeline | Project Manager

Basic pipeline (more like smart project folder structure) for small vfx projects.
Idea for this one is that it is very hard to come up with project folder structure that works for multiple applications. 
Usually you end up with a huge mess - files from different apps mixed together and hard to use relative paths (```../../../scene/textures/bricks.jpg```).
Another issue is when it comes time to clean things up for archiving - everything is mixed together. It's hard to know which files, sequences and temporary files are safe to remove (that can be easily re-generated if you need to work on the project in the future). 

I try to solve all of these issues with clever use of symlinks. It's a feature that is common in Linux/Unix/Mac based systems, where you can create "virtual" folders - folders that actually point to other folders that are located elswhere. This allows building paths relative to these virtual folders and not actual target folders. 

To use symlinks on Windows, you must have NTFS filesystem and enable developer mode in windows settings (Update & Security -> For developers -> Developer Mode : ON)

To simplify everything, I assume the following workflow:
1. You build Assets (Props, Characters, Environments etc.) and export (publish) final usable results (fbx, usd, abc, blend etc.) files in shared assets folder.
2. Each asset work files live in separate folder
   - Each asset or shot has a separate working folder (like a mini project) for each content creation app with a different internal folder structure suited for that app.
4. You should never reference files between work folders of different assets or shots directly
5. You only link or import thse finished assets into your shots or other assets scenes through shared folder.
   - Each asset or shot work folder contains links to shared folders – as if they are local in the work folder.
   - Each asset or shot work folder also contains links to shared render and temp folders where you can store rendered sequences or differenct caches 

Here is project structure explained in more detail: 
```
ProjectRoot
	Assets  [Assets shared between shots and apps]
			[ Don't use directly. Linked in work folders ]
		2D
			Artworks
		3D
			Fbx
				Ext_Models [link to External models library - i.e. photogrammetry folder on a server]
			Bgeo
			Obj
			Alembic
			USD
			C4D
			Blend
		Tex
			Ext [link to External texture library - i.e. texture library on a server]
		Lib
			Python_Libs

	Build [ Work folders for buildig assets, scenes, etc. ]
		Asset_Name_A
			[Houdini] - Houdini project
				Link: Assets/Tex
				Link: Assets/3d/Fbx,Bgeo,Obj,Alembic,USD
				Link: Render
				Link: Temp/Assets/Asset_Name_A Flip Geo Sim
			[Blender] - Blender project
				Link: Assets/Tex
				Link: Fbx,Obj,Alembic,USD
			[C4D] - C4D project
				Link: Assets/Tex
				Link: Fbx,Obj,Alembic,USD
			[Other] - Other 3d dcc app projects if needed (Zbrush, Marvellous etc.)
			Textures - Textuiring work (PSD files, Substance project etc.)
				Link: Shared/Tex
				
		Asset_Name_B
			...
			
	Shots [ Work folders for shots/scenes. Similar structure to asset work folders]
		Shot_XXYY 
			[Blender]
				Link: Assets/3d/fbx, obj, bgeo, alembic, Assets/Tex..
			[Houdini]
				Link: Assets/3d/fbx, obj, bgeo, alembic, Assets/Tex..
				Link: Temp/ShotX
				Link: Temp/Shared
			[Maya]
			[C4D]
			
			Comp [ Compositing projects - links folders from Render, 2D Assets, Preivs, Out]
				Link: Shared/2D/Artworks (Images needed for compositing)
				Link: Render/Shots/Shot_XXYY
				Link: Render/Previs/Shot_XXYY
				Link: Out (Project main output folder (deliver, images, previs, review)

	Render [Rendered Image sequences. Can remove when archiving to save space]
		Assets
			Asset_Name_A
			Asset_Name_B
		Previs
			Shot_SEQXXYY
		Shots
			Shot_SEQXXYY
	
	Out [ Valuable project outputs - easy to find in one place ]		
		Previs [all previs videos]
		Review [all "final" videos]
		Images [stills, screenshots, making of pics etc]
		Deliver - place for final deliveries
		
	Temp [ All temporary files - caches etc. Remove when archiving or saving space ]
		 [ Don't use directly. Linked in work folders ]
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
```


More here: http://www.rendereverything.com/symlinks/