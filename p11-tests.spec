# NOTE: package overrides CFLAGS with -O0 -g - that's OK for tests
Summary:	Library of test cases for PKCS#11 modules
Summary(pl.UTF-8):	Biblioteka przypadków testowych dla modułów PKCS#11
Name:		p11-tests
%define	snap	20110220
Version:	0.1
Release:	0.%{snap}.1
License:	BSD
Group:		Libraries
# git clone git://thewalter.net/p11-tests p11-tests
Source0:	%{name}-%{snap}.tar.xz
# Source0-md5:	b60108414b1ea83b52e85d3d4edca5e0
URL:		https://www.ohloh.net/p/p11-tests
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library of test cases for PKCS#11 modules.

%description -l pl.UTF-8
Biblioteka przypadków testowych dla modułów PKCS#11.

%package devel
Summary:	Header file for p11-tests library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki p11-tests
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for p11-tests library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki p11-tests.

%package static
Summary:	Static p11-tests library
Summary(pl.UTF-8):	Statyczna biblioteka p11-tests
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static p11-tests library.

%description static -l pl.UTF-8
Statyczna biblioteka p11-tests.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# --disable-stricts disables -Werror
%configure \
	--disable-strict
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libp11-tests.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING doc/pkcs11-coverage.txt
%attr(755,root,root) %{_bindir}/p11-tests
%attr(755,root,root) %{_libdir}/libp11-tests.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libp11-tests.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libp11-tests.so
%{_includedir}/p11-tests.h
%{_pkgconfigdir}/p11-tests.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libp11-tests.a
