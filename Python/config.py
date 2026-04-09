{

	"downloads" : [ "https://www.python.org/ftp/python/3.11.14/Python-3.11.14.tgz" ],

	"publicVariables" : {

		"pythonVersion" : "3.11",
		"pythonMajorVersion" : "3",
		"pythonMinorVersion" : "11",
		"pythonIncludeDir" : "{buildDir}/include/python{pythonVersion}",
		"pythonLibDir" : "{buildDir}/lib",

	},

	"url" : "https://www.python.org",

	"license" : "LICENSE",

	"dependencies" : [ "LibFFI", "ZLib" ],

	"environment" : {

		"LDFLAGS" : "-L{buildDir}/lib",
		"CPPFLAGS" : "-I{buildDir}/include",
		"LD_LIBRARY_PATH" : "{buildDir}/lib",

	},

	"commands" : [

		"./configure --prefix={buildDir} {libraryType} --with-ensurepip=install",
		"make -j {jobs}",
		"make install",

	],

	"manifest" : [

		"bin/python",
		"bin/python*[0-9]",

		"include/python*",

		"lib/libpython*{sharedLibraryExtension}*",
		"lib/Python.framework*",
		"lib/python{pythonVersion}",

	],

	"variables" : {

		"libraryType" : "--enable-shared",

	},

	"symbolicLinks" : [

		( "{buildDir}/bin/python", "python3" ),

	],

	"platform:macos" : {


		"variables" : {

			"libraryType" : "--enable-framework={buildDir}/lib",

		},

		"environment" : {

			"MACOSX_DEPLOYMENT_TARGET" : "12.0",

		},

		"publicVariables" : {


			"pythonIncludeDir" : "{buildDir}/lib/Python.framework/Headers",
			"pythonLibDir" : "{buildDir}/lib/Python.framework/Versions/{pythonVersion}/lib",

		},

		"symbolicLinks" : [

			( "{buildDir}/bin/python", "../lib/Python.framework/Versions/Current/bin/python{pythonMajorVersion}" ),
			( "{buildDir}/bin/python{pythonMajorVersion}", "../lib/Python.framework/Versions/Current/bin/python{pythonMajorVersion}" ),
			( "{buildDir}/bin/python{pythonVersion}", "../lib/Python.framework/Versions/Current/bin/python{pythonVersion}" ),
			( "{buildDir}/lib/Python.framework/Versions/Current/lib/libpython{pythonMajorVersion}.dylib", "libpython{pythonMajorVersion}.{pythonMinorVersion}.dylib" ),
		],

	},
	
	"platform:windows" : {

		"publicVariables" : {

			"pythonIncludeDir" : "{buildDir}/include",
			"pythonLibDir" : "{buildDir}/libs",

		},

		"environment" : {

			"PATH" : "{buildDir}\\bin;%PATH%",
			"DefaultWindowsSDKVersion" : "10.0.20348.0",

		},

		"commands" : [

			"call PCbuild/build.bat -p x64 --no-tkinter \"/p:PlatformToolset=v143\"",

			# Copy the directory layout to our build directory
			# "PCbuild\\amd64\\python.exe PC\\layout -s . -b PCbuild\\amd64 -v --precompile --include-pip --include-dev --include-stable --copy {buildDir}",

		],

		"postMovePaths" : {

			"{buildDir}/python.exe" : "{buildDir}/bin",
			"{buildDir}/python{pythonMajorVersion}{pythonMinorVersion}.dll" : "{buildDir}/bin",
			"{buildDir}/python{pythonMajorVersion}.dll" : "{buildDir}/bin",
			"{buildDir}/vcruntime*.dll" : "buildDir/bin",
			"externals/openssl-bin-1.1.1u/amd64/libcrypto.lib" : "{buildDir}/lib",
			"externals/openssl-bin-1.1.1u/amd64/libssl.lib" : "{buildDir}/lib",
			"externals/openssl-bin-1.1.u/amd64/include/opensll" : "{buildDir}/include",

		}

	},

}
