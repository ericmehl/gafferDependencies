{

	"downloads" : [

		"https://github.com/ImageEngine/cortex/archive/refs/tags/10.4.2.0.tar.gz"

	],

	"url" : "https://github.com/ImageEngine/cortex",

	"license" : "LICENSE",

	"dependencies" : [
		"Python", "OpenImageIO", "OpenEXR", "Boost", "OpenShadingLanguage",
		"Blosc", "FreeType", "GLEW", "Appleseed", "TBB", "OpenVDB", "USD", "Six"
	],

	"environment" : {

		"LD_LIBRARY_PATH" : "{buildDir}/lib",

	},

	"requiredEnvironment" : [ "RMAN_ROOT" ],

	"commands" : [

		"scons install"
			" -j {jobs}"
			" CXX=`which g++`"
			" CXXSTD=c++{c++Standard}"
			" INSTALL_PREFIX={buildDir}"
			" INSTALL_DOC_DIR={buildDir}/doc/cortex"
			" INSTALL_RMANPROCEDURAL_NAME={buildDir}/renderMan/procedurals/iePython"
			" INSTALL_RMANDISPLAY_NAME={buildDir}/renderMan/displayDrivers/ieDisplay"
			" INSTALL_PYTHON_DIR={buildDir}/python"
			" INSTALL_IECORE_OPS=''"
			" PYTHON_CONFIG={buildDir}/bin/python{pythonMajorVersion}-config"
			" PYTHON={buildDir}/bin/python"
			" BOOST_INCLUDE_PATH={buildDir}/include/boost"
			" LIBPATH={buildDir}/lib"
			" BOOST_LIB_SUFFIX=''"
			" OPENEXR_INCLUDE_PATH={buildDir}/include"
			" ILMBASE_INCLUDE_PATH={buildDir}/include"
			" VDB_INCLUDE_PATH={buildDir}/include"
			" TBB_INCLUDE_PATH={buildDir}/include"
			" OIIO_INCLUDE_PATH={buildDir}/include"
			" OSL_INCLUDE_PATH={buildDir}/include"
			" BLOSC_INCLUDE_PATH={buildDir}/include"
			" FREETYPE_INCLUDE_PATH={buildDir}/include/freetype2"
			" WITH_GL=1"
			" GLEW_INCLUDE_PATH={buildDir}/include/GL"
			" RMAN_ROOT=$RMAN_ROOT"
			" NUKE_ROOT="
			" APPLESEED_ROOT={buildDir}/appleseed"
			" APPLESEED_INCLUDE_PATH={buildDir}/appleseed/include"
			" APPLESEED_LIB_PATH={buildDir}/appleseed/lib"
			" USD_LIB_PREFIX=usd_"
			" ENV_VARS_TO_IMPORT='LD_LIBRARY_PATH TERM'"
			" OPTIONS=''"
			" {extraArgs}"
			" SAVE_OPTIONS=gaffer.options",

		# Symlink for RenderMan, which uses a different convention to 3Delight.
		"ln -s -f ieDisplay{sharedLibraryExtension} {buildDir}/renderMan/displayDrivers/d_ieDisplay.so"

	],

	"manifest" : [

		"include/IECore*",
		"lib/libIECore*{sharedLibraryExtension}",
		"python/IECore*",
		"renderMan",
		"appleseedDisplays",
		"glsl/IECoreGL",
		"glsl/*.frag",
		"glsl/*.vert",

	],

	"variables" : {

		"extraArgs" : "",

	},

	"platform:macos" : {

		"variables" : {

			# On Mac, `python3-config --ldflags` is broken, so we specify the flags explicitly.
			"extraArgs" :
				" PYTHON_LIB_PATH={buildDir}/lib/Python.framework/Versions/{pythonVersion}/lib"
				" PYTHON_LINK_FLAGS=-lpython{pythonVersion}"

		},

	},


}
