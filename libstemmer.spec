Summary:	The C version of the libstemmer library
Summary(pl.UTF-8):	Wersja C biblioteki libstemmer
Name:		libstemmer
Version:	20141109
Release:	3
License:	BSD
Group:		Libraries
Source0:	http://snowball.tartarus.org/dist/%{name}_c.tgz
# Source0-md5:	6f32f8f81cd6fa0150333ab540af5e27
Patch0:		%{name}-makefile.patch
Patch1:		libtool-tag.patch
Patch2:		optflags.patch
URL:		http://snowball.tartarus.org/
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Snowball is a small string processing language designed for creating
stemming algorithms for use in Information Retrieval.

This package contains the C version of the libstemmer library.

%description -l pl.UTF-8
Snowball to niewielki język przetwarzania łańcuchów znaków,
zaprojektowany do tworzenia algorytmów określających tematy wyrazów,
wykorzystywanych przy wyszukiwaniu informacji.

%package devel
Summary:	Header files for libstemmer library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libstemmer
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libstemmer library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libstemmer.

%package static
Summary:	Static libstemmer library
Summary(pl.UTF-8):	Statyczna biblioteka libstemmer
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libstemmer library.

%description static -l pl.UTF-8
Statyczna biblioteka libstemmer.

%package utils
Summary:	The stemwords utility using the libstemmer library
Summary(pl.UTF-8):	Narzędzie stemwords korzystające z biblioteki libstemmer
Group:		Applications/Text

%description utils
The stemwords utility using the libstemmer library

%description utils -l pl.UTF-8
Narzędzie stemwords korzystające z biblioteki libstemmer.

%prep
%setup -qc
mv %{name}_c/* .
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	CC="%{__cc}" \
	libdir=%{_libdir} \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	libdir=%{_libdir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libstemmer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libstemmer.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libstemmer.so
%{_libdir}/libstemmer.la
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/libstemmer.a

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/stemwords
