%include	/usr/lib/rpm/macros.perl
Summary:	A utility to filter the daily newsletter from freshmeat.net
Summary(pl):	Narzêdzie do filtrowania codziennego newslettera z freshmeat.net
Name:		whatsnewfm
Version:	0.6.2
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://www.cgarbs.de/stuff/%{name}-%{version}.tar.gz
# Source0-md5:	532704221b9079ffa8bb9f26eb5899d4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch
%description
whatsnewfm is a utility to filter the daily newsletter from
freshmeat.net

The main purpose is to cut the huge newsletter to a smaller size by
only showing items that you didn't see before.
The items already seen will be stored in a database. After some time,
the items expire and will be shown again the next time they are
included in a newsletter.
If you find an item that you consider particularly useful, you can add
it to a "hot" list. Items in the hot list are checked for updates so
that you don't miss anything about your favourite programs.
%description -l pl
whatsnewfm jest narzêdziem do filtrowania codziennego newslettera z 
freshmeat.net

G³ownym jego celem jest przycinanie ogromnych newsletterów poprzez
pokazywanie tylko tych elementów, których jeszcze nie widzia³e¶.
Widziane elementy s± przechowywane w bazie danych. Po jakim¶ czasie jednak
elementy te wygasaj± i zostan± znowu pokazane, gdy tylko siê pojawi±.
Gdy który¶ z elementów ciê interesuje, mo¿esz go dodaæ do tzw. hotlisty.
Elementy z hotlisty s± sprawdzane za ka¿dym razem, wiêc nie musisz siê
martwiæ, ¿e omin± ciê jakiekolwiek informacje o twoim ulubionym programie.
%prep
%setup -q
%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}/
cp whatsnewfm.pl $RPM_BUILD_ROOT%{_bindir}/
install -d $RPM_BUILD_ROOT%{_prefix}/man/man1/
pod2man whatsnewfm.pl | gzip -9 > $RPM_BUILD_ROOT%{_prefix}/man/man1/whatsnewfm.pl.1.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING HISTORY whatsnewfmrc.sample welcome
%attr(755,root,root) %{_bindir}/whatsnewfm.pl
%{_prefix}/man/man1/whatsnewfm.pl.1.gz
