{

	"downloads" : [

		"https://github.com/openexr/openexr/releases/download/v2.3.0/ilmbase-2.3.0.tar.gz"

	],

	"license" : "LICENSE",

	"commands" : [

		"./configure --prefix={buildDir}",
		"make -j {jobs}",
		"make install",

	],

	"platform:windows" : {

		"variables" : {
			"cmakeGenerator" : "\"Visual Studio 15 2017 Win64\"",
		},

		"commands" : [

			"mkdir gafferBuild",
			"cd gafferBuild && "
				" cmake"
				" -Wno-dev"
				" -G {cmakeGenerator}"
				" -D OPENEXR_BUILD_SHARED=ON"	# this will change to BUILD_SHARED_LIBS=ON post 2.3.0
				" -D CMAKE_INSTALL_PREFIX={buildDir}"
				" ..",
			"cd gafferBuild && cmake --build . --config {cmakeBuildType} --target install -j {jobs}",
		]
	}

}
