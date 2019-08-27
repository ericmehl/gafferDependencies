{

	"downloads" : [

		"https://github.com/openexr/openexr/releases/download/v2.2.0/openexr-2.2.0.tar.gz"

	],

	"license" : "OpenEXR/LICENSE",

	"commands" : [

		"./configure --prefix={buildDir}",
		"make -j {jobs}",
		"make install",

	],

	"platform:windows" : {

		"variables" : {
			"cmakeGenerator" : "\"Visual Studio 15 2017 Win64\"",
		},

		"downloads" : [

			"https://github.com/openexr/openexr/archive/v2.2.0.zip"

		],

		"environment" : {

			"PATH" : "{buildDir}\\bin;{buildDir}\\lib;%PATH%",

		},

		"commands" : [
			"cd IlmBase && mkdir gafferBuild",
			"cd IlmBase\\gafferBuild && cmake"
				" -D CMAKE_INSTALL_PREFIX={buildDir}"
				" -D CMAKE_BUILD_TYPE={cmakeBuildType}"
				" -G {cmakeGenerator}"
				" -D CMAKE_PREFIX_PATH={buildDir}"
				" -D OPENEXR_PACKAGE_PREFIX={buildDir}"
				# " -D OPENEXR_NAMESPACE_VERSIONING=OFF"
				" -D OPENEXR_BUILD_TESTS=OFF"
				" ..",
			"cd IlmBase\\gafferBuild && cmake --build . --config {cmakeBuildType} --target install",
			"cd PyIlmBase && mkdir gafferBuild",
			"cd PyIlmBase\\gafferBuild && cmake"
				" -D CMAKE_INSTALL_PREFIX={buildDir}"
				" -D CMAKE_BUILD_TYPE={cmakeBuildType}"
				" -G {cmakeGenerator}"
				" -D CMAKE_PREFIX_PATH={buildDir}"
				" -D ILMBASE_PACKAGE_PREFIX={buildDir}"
				# " -D OPENEXR_NAMESPACE_VERSIONING=OFF"
				" -D OPENEXR_BUILD_TESTS=OFF"
				" ..",
			"cd PyIlmBase\\gafferBuild && cmake --build . --config {cmakeBuildType} --target install",
			"cd OpenEXR && mkdir gafferBuild",
			"cd OpenEXR\\gafferBuild && cmake"
				" -D CMAKE_INSTALL_PREFIX={buildDir}"
				" -D CMAKE_BUILD_TYPE={cmakeBuildType}"
				" -G {cmakeGenerator}"
				" -D CMAKE_PREFIX_PATH={buildDir}"
				" -D ILMBASE_PACKAGE_PREFIX={buildDir}"
				# " -D OPENEXR_NAMESPACE_VERSIONING=OFF"
				" -D OPENEXR_BUILD_TESTS=OFF"
				" ..",
			"cd OpenEXR\\gafferBuild && cmake --build . --config {cmakeBuildType} --target install",
			"if not exist {buildDir}\\python mkdir {buildDir}\\python",
			"copy {buildDir}\\lib\\python2.7\\site-packages\\iex.pyd {buildDir}\\python\\iex.pyd",
			"copy {buildDir}\\lib\\python2.7\\site-packages\\imath.pyd {buildDir}\\python\\imath.pyd",
		]
	},

}
