#
# Conditional build:
%bcond_with		gtk3		# build GTK+3 disables GTK+2
%bcond_without		gtk2	# build with GTK+2

%if %{with gtk3}
%undefine	with_gtk2
%endif

Summary:	lxauncher
Name:		lxlauncher
Version:	0.2.2
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	16df627447838b170a72cc3a9ee21497
URL:		http://wiki.lxde.org/en/LXLauncher
BuildRequires:	gettext-devel
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.12.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	menu-cache-devel
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LXLauncher is an open source clone of Asus launcher for EeePC. It
outperformes the original launcher developed by Xandros.

%prep
%setup -q

%build
%configure \
	%{?with_gtk3:--enable-gtk3}
touch po/stamp-it
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# there is ur locale so drop ur_PK
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%{_sysconfdir}/xdg/lxlauncher
%{_sysconfdir}/xdg/menus/lxlauncher-applications.menu
%attr(755,root,root) %{_bindir}/lxlauncher
%{_datadir}/desktop-directories/*directory
