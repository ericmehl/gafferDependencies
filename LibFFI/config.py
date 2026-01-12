{

	"downloads" : [

		"https://github.com/libffi/libffi/releases/download/v3.4.2/libffi-3.4.2.tar.gz"

	],

	"url" : "https://sourceware.org/libffi/",
	"license" : "LICENSE",

	"commands" : [

		"sh configure {preArgs} --prefix={buildDir} --libdir={buildDir}/lib {postArgs}",
		"make -j {jobs}",
		"make install",

	],

	"manifest" : [

		"lib/libffi*{sharedLibraryExtension}*",

	],

	"variables" : {

		"preArgs" : "",
		"postArgs" : "--disable-multi-os-directory --without-gcc-arch",

	},

	"platform:windows" : {

		"variables" : {

			"preArgs" : '--enable-shared --build x86_64-w64-mingw32 --host x86_64-w64-mingw32 CC="../msvcc.sh -m64" CXX="../msvcc.sh -m64" LD=link CPP="cl -nologo -EP" CXXCPP="cl -nologo -EP" CPPFLAGS="-DFFI_BUILDING_DLL" AR=\'../.ci/ar-lib lib\' NM=\'dumpbin -symbols\' STRIP=\':\'',
			"postArgs" : "",

		},

	},

}
