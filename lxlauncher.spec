#
# Conditional build:
%bcond_with	gtk3	# use GTK+3 instead of GTK+2

Summary:	Open source clone of Asus launcher for EeePC
Summary(pl.UTF-8):	Mający otwarte źródła klon Asus launchera dla EeePC
Name:		lxlauncher
Version:	0.2.5
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
# Source0-md5:	94a7a36af92f8409365b6a25b6904eeb
URL:		http://www.lxde.org/
BuildRequires:	gettext-tools
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2:2.12.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0.0}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	menu-cache-devel
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.12.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LXLauncher is an open source clone of Asus launcher for EeePC. It
outperformes the original launcher developed by Xandros.

%description -l pl.UTF-8
LXLauncher to mający otwarte źródła klon Asus launchera dla EeePC.
Działa lepiej niż oryginał stworzony przez firmę Xandros.

%prep
%setup -q

%build
%configure \
	%{?with_gtk3:--enable-gtk3}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# unify name
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{tt_RU,tt}
# not supported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/frp
# just a copy of ur
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%{_sysconfdir}/xdg/lxlauncher
%{_sysconfdir}/xdg/menus/lxlauncher-applications.menu
%attr(755,root,root) %{_bindir}/lxlauncher
%{_datadir}/desktop-directories/*directory
%{_mandir}/man1/lxlauncher.1*
