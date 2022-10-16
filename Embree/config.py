{

	"downloads" : [

		"https://github.com/embree/embree/archive/v3.13.3.tar.gz"

	],

	"url" : "https://www.embree.org/",

	"license" : "LICENSE.txt",

	"dependencies" : [ "TBB" ],

	"commands" : [

		"mkdir gafferBuild",
		"cd gafferBuild &&"
			" cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D CMAKE_INSTALL_LIBDIR={buildDir}/lib"
			" -D EMBREE_TBB_ROOT={buildDir}"
			" -D EMBREE_STATIC_LIB=OFF"
			" -D EMBREE_ISPC_SUPPORT=OFF"
			" -D EMBREE_TUTORIALS=OFF"
			" -D EMBREE_RAY_MASK=ON"
			" -D EMBREE_FILTER_FUNCTION=ON"
			" -D EMBREE_BACKFACE_CULLING=OFF"
			" -D EMBREE_TASKING_SYSTEM=TBB"
			" ..",
		"cd gafferBuild && make install -j {jobs} VERBOSE=1",

	],

	"manifest" : [

		"include/embree3",

		"lib/{libraryPrefix}embree3*{sharedLibraryExtension}*",
		
		"lib/{libraryPrefix}embree3*.lib",

	],

	"platform:windows" : {

		"commands" : [

			"mkdir gafferBuild",
			"cd gafferBuild && cmake"
				" -G {cmakeGenerator}"
				" -D CMAKE_INSTALL_PREFIX={buildDir}"
				" -D CMAKE_PREFIX_PATH={buildDir}"
				" -D CMAKE_INSTALL_LIBDIR={buildDir}/lib"
				" -D TBB_ROOT={buildDir}"
				" -D EMBREE_STATIC_LIB=OFF"
				" -D EMBREE_ISPC_SUPPORT=OFF"
				" -D EMBREE_TUTORIALS=OFF"
				" -D EMBREE_RAY_MASK=ON"
				" -D EMBREE_FILTER_FUNCTION=ON"
				" -D EMBREE_BACKFACE_CULLING=OFF"
				" -D EMBREE_TASKING_SYSTEM=TBB"

				# " -D CMAKE_INSTALL_INCLUDEDIR={buildDir}/include"
				# " -D CMAKE_INSTALL_DATAROOTDIR="
				# " -D CMAKE_INSTALL_DOCDIR=doc"
				# " -D CMAKE_INSTALL_BINDIR=bin"
				" ..",
			"cd gafferBuild && cmake --build . --config {cmakeBuildType} --target install",
			"move {buildDir}\\bin\\{libraryPrefix}embree3*{sharedLibraryExtension}* {buildDir}\\lib"
		]

	},

}
