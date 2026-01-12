{

	"downloads" : [

		"https://github.com/libffi/libffi/releases/download/v3.4.2/libffi-3.4.2.tar.gz"

	],

	"url" : "https://sourceware.org/libffi/",
	"license" : "LICENSE",

	"commands" : [

		"sh configure {args} -prefix={buildDir} --libdir={buildDir}/lib",
		"make -j {jobs}",
		"{installCommand}",

	],

	"manifest" : [

		"lib/libffi*{sharedLibraryExtension}*",

	],

	"variables" : {

		"args" : "--disable-multi-os-directory --without-gcc-arch",
		"installCommand" : "make install",

	},

	"platform:windows" : {

		"variables" : {

			"host" : "x86_64-w64-cygwin",
			"args" : "CC='../msvcc.sh -m64' CXX='../msvcc.sh -m64' LD='link' CPP='cl -nologo -EP' CXXCPP='cl -nologo -EP' CPPFLAGS='-DFFI_BUILDING_DLL' AR='../.travis/ar-lib lib' NM='dumpbin -symbols' STRIP=':' --build={host} --host={host} --disable-static --enable-shared",
			"installCommand" : "",

		},

		"postBuildCopy" : [

			( "{host}/include", "*.h", "{buildDir}/include" ),
			( "{host}/.libs", "libffi-8.*", "{buildDir}/lib" ),

		]

	},

}
