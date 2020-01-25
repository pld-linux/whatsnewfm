Summary:	A utility to filter the daily newsletter from freshmeat.net
Summary(pl.UTF-8):	Narzędzie do filtrowania codziennego newslettera z freshmeat.net
Name:		whatsnewfm
Version:	0.6.5
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://www.cgarbs.de/stuff/%{name}-%{version}.tar.gz
# Source0-md5:	6c9123b50a1b3238a7f9fb9f0b440759
BuildRequires:	perl-tools-pod
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
whatsnewfm is a utility to filter the daily newsletter from
freshmeat.net.

The main purpose is to cut the huge newsletter to a smaller size by
only showing items that you didn't see before. The items already seen
will be stored in a database. After some time, the items expire and
will be shown again the next time they are included in a newsletter.
If you find an item that you consider particularly useful, you can add
it to a "hot" list. Items in the hot list are checked for updates so
that you don't miss anything about your favourite programs.

%description -l pl.UTF-8
whatsnewfm jest narzędziem do filtrowania codziennego newslettera z
freshmeat.net.

Głownym jego celem jest przycinanie ogromnych newsletterów poprzez
pokazywanie tylko tych elementów, których użytkownik jeszcze nie
widział. Widziane elementy są przechowywane w bazie danych. Po jakimś
czasie jednak elementy te wygasają i zostaną znowu pokazane, gdy tylko
się pojawią. Gdy któryś z elementów jest interesujący, można go dodać
do tzw. hotlisty. Elementy z hotlisty są sprawdzane za każdym razem,
więc nie trzeba się martwić, że zostaną pominięte jakiekolwiek
informacje o ulubionym programie.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install whatsnewfm.pl $RPM_BUILD_ROOT%{_bindir}

pod2man whatsnewfm.pl > $RPM_BUILD_ROOT%{_mandir}/man1/whatsnewfm.pl.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README HISTORY whatsnewfmrc.sample welcome
%attr(755,root,root) %{_bindir}/whatsnewfm.pl
%{_mandir}/man1/whatsnewfm.pl.1*
