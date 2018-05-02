{

	"downloads" : [

		"https://github.com/madler/zlib/archive/v1.2.11.tar.gz"

	],

	"commands" : [

		"mkdir gafferBuild",

		"cd gafferBuild &&"
			" cmake"
			" -G {cmakeGenerator}"
			" -D CMAKE_BUILD_TYPE={cmakeBuildType}"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" ..",

		"cd gafferBuild && cmake --build . --config {cmakeBuildType} --target install -- -j {jobs}"

	],

}
