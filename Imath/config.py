{

	"downloads" : [

		"https://github.com/AcademySoftwareFoundation/Imath/archive/refs/tags/v3.1.7.tar.gz"

	],

	"url" : "http://www.openexr.com",

	"license" : "LICENSE.md",

	"dependencies" : [ "Python", "Boost" ],

	"environment" : {

		"PATH" : "{buildDir}/bin:$PATH",
		"LD_LIBRARY_PATH" : "{buildDir}/lib",

	},

	"commands" : [

		"cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			# OpenEXR's CMake setup uses GNUInstallDirs, which unhelpfully
			# puts the libraries in `lib64`. Coax them back.
			" -D CMAKE_INSTALL_LIBDIR={buildDir}/lib"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D PYTHON=ON"
			" -D Boost_NO_SYSTEM_PATHS=TRUE"
			" -D Boost_NO_BOOST_CMAKE=TRUE"
			" -D BOOST_ROOT={buildDir}"
			" -D Python_ROOT_DIR={buildDir}"
			" -D Python3_ROOT_DIR={buildDir}"
			" -D Python3_FIND_STRATEGY=LOCATION"
			" -D PYIMATH_OVERRIDE_PYTHON_INSTALL_DIR={buildDir}/python"
			" ."
		,

		"make VERBOSE=1 -j {jobs}",
		"make install",

	],

	"manifest" : [

		"include/Imath",
		"lib/{libraryPrefix}Imath*{sharedLibraryExtension}*",
        "lib/{libraryPrefix}Imath*.lib",
		"lib/{libraryPrefix}PyImath*{sharedLibraryExtension}*",
        "lib/{libraryPrefix}PyImath*.lib",
		"python/imath.{pythonModuleExtension}",

	],
    
	"platform:windows" : {

		"variables" : {

			"cmakeGenerator" : "\"Visual Studio 17 2022\"",

		},

		"dependencies" : [ "Python", "Boost", ],

		"commands" : [
			"mkdir gafferBuild",
			"cd gafferBuild && cmake"
				" -G {cmakeGenerator}"
				" -D CMAKE_INSTALL_PREFIX={buildDir}"
				" -D CMAKE_BUILD_TYPE={cmakeBuildType}"
				" -D CMAKE_PREFIX_PATH={buildDir}"
                " -D IMATH_LIB_SUFFIX="
                " -D PYTHON=ON"
				" -D Boost_NO_SYSTEM_PATHS=TRUE"
				" -D Boost_NO_BOOST_CMAKE=TRUE"
				" -D BOOST_ROOT={buildDir}"
				" -D Python3_ROOT_DIR={buildDir}"
				" -D Python_NO_SYSTEM_PATHS=TRUE"
				" -D Python3_FIND_STRATEGY=LOCATION"
				" -D CMAKE_CXX_FLAGS=\"-DBOOST_ALL_NO_LIB -DHAVE_SNPRINTF\""
				" ..",
			"cd gafferBuild && cmake --build . --config {cmakeBuildType} --target install",
			"if not exist {buildDir}\\python mkdir {buildDir}\\python",
			"copy {buildDir}\\lib\\site-packages\\imath.pyd {buildDir}\\python\\imath.pyd",
			"copy {buildDir}\\bin\\{libraryPrefix}Imath*{sharedLibraryExtension}* {buildDir}\\lib\\",
			"copy {buildDir}\\bin\\{libraryPrefix}PyImath*{sharedLibraryExtension}* {buildDir}\\lib\\",
		]
	},

}
