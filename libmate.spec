%define api	2
%define major	0
%define libname	%mklibname mate %{api} %{major}
%define devname	%mklibname -d mate

Summary:	MATE libraries
Name:		libmate
Version:	1.2.0
Release:	1
Group:		System/Libraries
License:	LGPLv2+
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz

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
%apply_patches

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

