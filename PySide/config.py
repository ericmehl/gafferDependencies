{

	"downloads" : [

		"https://www.autodesk.com/content/dam/autodesk/www/Company/files/PySide2-Maya-2018_6.tgz"

	],

	"license" : "LICENSE.LGPLv21",

	"environment" : {

		"PATH" : "{buildDir}/bin:$PATH",

	},

	"commands" : [

		"python setup.py --ignore-git --no-examples --jobs {jobs} --osx-use-libc++ install"


	],

	"platform:linux" : {

		"environment" : {

			"LD_LIBRARY_PATH" : "{buildDir}/lib",

		},

	},

	"platform:osx" : {

		"environment" : {

			"DYLD_FRAMEWORK_PATH" : "{buildDir}/lib",

		},

	},

	"platform:windows" : {

		"environment" : {

			"PATH" : "{buildDir}\\bin;{buildDir}\\lib;%PATH%",
			"PYTHONHOME" : "{buildDir}",
			"PYTHONPATH" : "{buildDir}\\python;%PYTHONPATH%",

		},

		"commands" : [
			"python setup.py install"
				" --ignore-git"
				" --qmake=%BUILD_DIR%\\bin\\qmake.exe"
				" --openssl=%BUILD_DIR%\\lib"
				" --cmake=\"C:\\Program Files\\CMake\\bin\\cmake.exe\""
				" --jobs {jobs}"
				" --no-examples",
		]
	},

}
