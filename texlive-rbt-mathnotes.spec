Name:		texlive-rbt-mathnotes
Version:	61193
Release:	1
Summary:	Rebecca Turner's personal macros and styles for typesetting mathematics notes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rbt-mathnotes
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rbt-mathnotes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rbt-mathnotes.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Styles for typesetting mathematics notes. Includes document
classes for typesetting homework assignments and "formula cheat
sheets" for exams. Several examples are included, along with
rendered PDFs.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/rbt-mathnotes
%doc %{_texmfdistdir}/doc/latex/rbt-mathnotes

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
