{

	"downloads" : [

		"https://github.com/openexr/openexr/releases/download/v2.3.0/openexr-2.3.0.tar.gz"

	],

	"license" : "LICENSE",

	"commands" : [

		"./configure --prefix={buildDir}",
		"make -j {jobs}",
		"make install",

	],

	"platform:windows" : {

		"downloads" : [

			"https://github.com/openexr/openexr/archive/v2.3.0.zip"

		],


		"commands" : [
			"mkdir gafferBuild",
			"cd gafferBuild && cmake"
				" -DCMAKE_INSTALL_PREFIX={buildDir}"
				" .."
				" -G {cmakeGenerator}"
				# " -D OPENEXR_BUILD_ILMBASE=OFF"
				# " -D OPENEXR_BUILD_OPENEXR=ON"
				# " -D OPENEXR_BUILD_PYTHON_LIBS=ON"
				# " -D OPENEXR_BUILD_VIEWERS=OFF"
				" -DCMAKE_PREFIX_PATH={buildDir}"
				# " -D BOOST_ROOT={buildDir}"
				# " -D Boost_INCLUDE_DIRS={buildDir}\\include\\boost-1_61"
				# " -D PYTHON_INCLUDE_PATH={buildDir}\\include"
				# " -D ILMBASE_PACKAGE_PREFIX={buildDir}"
				# " -D ILMBASE_LOCATION={buildDir}"
				" ..",
			"cd gafferBuild && cmake --build . --config {cmakeBuildType} --target install -j {jobs}",
		]
	},

}
