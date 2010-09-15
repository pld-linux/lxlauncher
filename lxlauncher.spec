Summary:	lxauncher
Name:		lxlauncher
Version:	0.2.1
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	5dbe6076eb1a411278e1fc2bccf2d75d
Patch0:		%{name}-0.2.1-fix-segfault.patch
URL:		http://wiki.lxde.org/en/LXLauncher
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.12.0
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
%patch0 -p0

%build
%configure
touch po/stamp-it
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
