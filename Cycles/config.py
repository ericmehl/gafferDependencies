{

	"downloads" : [

		"https://github.com/blender/cycles/archive/refs/tags/v3.2.0.tar.gz",

	],

	"url" : "https://www.cycles-renderer.org/",

	"license" : "LICENSE",

	"dependencies" : [ "Boost", "OpenJPEG", "OpenImageIO", "TBB", "Alembic", "Embree", "OpenColorIO", "OpenVDB", "OpenShadingLanguage", "USD" ],

	"commands" : [

		"mkdir build",
		"cd build &&"
			" cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}/cycles"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D CMAKE_BUILD_TYPE=Release"
			" -D WITH_CYCLES_OPENIMAGEDENOISE=OFF"
			" -D WITH_CYCLES_DEVICE_CUDA=OFF"
			" -D WITH_CYCLES_DEVICE_OPTIX=OFF"
			" -D CMAKE_POSITION_INDEPENDENT_CODE=ON"
			" -D PXR_ROOT={buildDir}"
			" ..",
		"cd build && make install -j {jobs} VERBOSE=1",

		"mkdir -p {buildDir}/cycles/include",
		"cd src && find . -name '*.h' | cpio -pdm {buildDir}/cycles/include",
		"cp -r third_party/atomic/* {buildDir}/cycles/include",
		"mkdir -p {buildDir}/cycles/bin",
		"mv {buildDir}/cycles/cycles {buildDir}/cycles/bin/cycles",
		"cp -r build/lib {buildDir}/cycles",

	],

	"manifest" : [

		"cycles",

	],

	"platform:windows" : {

		"commands" : [

			"mkdir build",
			"cd build &&"
				" cmake"
				" -W-nodev -G {cmakeGenerator}"
				" -D CMAKE_INSTALL_PREFIX={buildDir}/cycles"
				" -D CMAKE_PREFIX_PATH={buildDir}"
				" -D CMAKE_BUILD_TYPE={cmakeBuildType}"
				" -D WITH_CYCLES_OPENIMAGEDENOISE=OFF"
				" -D WITH_CYCLES_DEVICE_CUDA=OFF"
				" -D WITH_CYCLES_DEVICE_OPTIX=OFF"
				" -D CMAKE_POSITION_INDEPENDENT_CODE=ON"
				" -D TBB_ROOT_DIR={buildDirFwd}"
				" -D OPENVDB_ROOT_DIR={buildDirFwd}"
				" -D NANOVDB_INCLUDE_DIR={buildDirFwd}/include"
				" -D GLEW_ROOT_DIR={buildDirFwd}"
				" ..",
			"set PATH={buildDir}/lib;%PATH% && cd build && cmake --build . --config {cmakeBuildType} --target install -- -j {jobs}",
			"if not exist \"{buildDir}\\cycles\\bin\" mkdir {buildDir}\\cycles\\bin",
			"if not exist \"{buildDir}\\cycles\\include\" mkdir {buildDir}\\cycles\\include",
			"copy build\\bin\\cycles.* {buildDir}\\cycles\\bin",
			"xcopy /sehyi build\\lib {buildDir}\\cycles\\lib",
			"xcopy /sehyi third_party\\atomic\\* {buildDir}\\cycles\\include",
			"xcopy /shyi src\\*.h K:\\build\\gaffer\\cycles\\include",

		]

	}

}
