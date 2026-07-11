%global tl_name rbt-mathnotes
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.2
Release:	%{tl_revision}.1
Summary:	Rebecca Turners personal macros and styles for typesetting mathematics notes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/rbt-mathnotes
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rbt-mathnotes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rbt-mathnotes.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Styles for typesetting mathematics notes. Includes document classes for
typesetting homework assignments and "formula cheat sheets" for exams.
Several examples are included, along with rendered PDFs.

