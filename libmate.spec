%define api	2
%define major	0
%define libname	%mklibname mate %{api} %{major}
%define devname	%mklibname -d mate

Summary:	MATE libraries
Name:		libmate
Version:	1.4.0
Release:	1
Group:		System/Libraries
License:	LGPLv2+
URL:		https://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires: gtk-doc
BuildRequires: intltool
BuildRequires: mate-conf
BuildRequires: mate-common
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(libmatecomponent-2.0)
BuildRequires: pkgconfig(mateconf-2.0)
BuildRequires: pkgconfig(mate-vfs-2.0)
BuildRequires: pkgconfig(popt)

# no canberra-gtk2
Requires:	canberra-common
Requires:	libmatecomponent
Requires:	%{name}-schemas >= %{version}-%{release}

%description
Data files for the MATE library such as translations.

%package schemas
Summary:	Default configuration for some MATE software
Group:		%{group}
Requires:	mate-conf

%description schemas
Default configuration for MATE software

%package -n %{libname}
Summary:	Shared libraries for MATE applications
Group:		%{group}

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{devname}
Summary:	Development libraries, include files for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description -n %{devname}
Development library and headers files for %{name}.

%prep
%setup -q
%autopatch -p1

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static \
	--disable-schemas-install

%make

%install
%makeinstall_std

# remove unpackaged files
find %{buildroot} -name '*.la' | xargs rm

%find_lang %{name}

%files -f %{name}.lang
%config(noreplace) %{_sysconfdir}/sound/events/*
%{_bindir}/mate-open
%{_libdir}/matecomponent/monikers/*.so
%{_libdir}/matecomponent/servers/*
%{_datadir}/mate-background-properties/mate-default.xml
%{_mandir}/man7/*

%files -n %{libname}
%{_libdir}/libmate-%{api}.so.%{major}*

%files -n %{devname}
%doc ChangeLog NEWS 
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so

%files schemas
%{_sysconfdir}/mateconf/schemas/desktop_mate_*.schemas



%changelog
* Fri Jul 27 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.4.0-1
+ Revision: 811351
- new version 1.4.0

* Tue Jun 12 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-2
+ Revision: 805266
- rebuild adding requires to make MATE work

* Thu May 31 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-1
+ Revision: 801598
- imported package libmate

