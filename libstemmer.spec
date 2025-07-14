Summary:	The C version of the libstemmer library
Summary(pl.UTF-8):	Wersja C biblioteki libstemmer
Name:		libstemmer
Version:	2.2.0
Release:	1
Epoch:		1
License:	BSD
Group:		Libraries
#Source0Download: https://snowballstem.org/download.html
Source0:	https://snowballstem.org/dist/%{name}_c-%{version}.tar.gz
# Source0-md5:	a0add7c0ebdd8d18872a31199bf37f4d
Patch0:		%{name}-makefile.patch
URL:		https://snowballstem.org/
BuildRequires:	libtool >= 2:1.5
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
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for libstemmer library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libstemmer.

%package static
Summary:	Static libstemmer library
Summary(pl.UTF-8):	Statyczna biblioteka libstemmer
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

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
%setup -q -n %{name}_c-%{version}
%patch -P0 -p1

%build
CFLAGS="%{rpmcflags}" \
CPPFLAGS="%{rpmcppflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} \
	CC="%{__cc}" \
	libdir=%{_libdir}

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
%doc COPYING NEWS README
%attr(755,root,root) %{_libdir}/libstemmer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libstemmer.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libstemmer.so
%{_libdir}/libstemmer.la
%{_includedir}/libstemmer

%files static
%defattr(644,root,root,755)
%{_libdir}/libstemmer.a

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/stemwords
