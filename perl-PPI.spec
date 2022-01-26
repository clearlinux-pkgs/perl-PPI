#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-PPI
Version  : 1.271
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/PPI-1.271.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/PPI-1.271.tar.gz
Summary  : 'Parse, Analyze and Manipulate Perl (without perl)'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-PPI-perl = %{version}-%{release}
Requires: perl(IO::String)
Requires: perl(Params::Util)
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Inspector)
BuildRequires : perl(Clone)
BuildRequires : perl(IO::String)
BuildRequires : perl(Params::Util)
BuildRequires : perl(Task::Weaken)
BuildRequires : perl(Test::Deep)
BuildRequires : perl(Test::NoWarnings)
BuildRequires : perl(Test::Object)
BuildRequires : perl(Test::SubCalls)

%description
This archive contains the distribution PPI,
version 1.271:
Parse, Analyze and Manipulate Perl (without perl)

%package dev
Summary: dev components for the perl-PPI package.
Group: Development
Provides: perl-PPI-devel = %{version}-%{release}
Requires: perl-PPI = %{version}-%{release}

%description dev
dev components for the perl-PPI package.


%package perl
Summary: perl components for the perl-PPI package.
Group: Default
Requires: perl-PPI = %{version}-%{release}

%description perl
perl components for the perl-PPI package.


%prep
%setup -q -n PPI-1.271
cd %{_builddir}/PPI-1.271

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/PPI.3
/usr/share/man/man3/PPI::Cache.3
/usr/share/man/man3/PPI::Document.3
/usr/share/man/man3/PPI::Document::File.3
/usr/share/man/man3/PPI::Document::Fragment.3
/usr/share/man/man3/PPI::Document::Normalized.3
/usr/share/man/man3/PPI::Dumper.3
/usr/share/man/man3/PPI::Element.3
/usr/share/man/man3/PPI::Exception.3
/usr/share/man/man3/PPI::Find.3
/usr/share/man/man3/PPI::Lexer.3
/usr/share/man/man3/PPI::Node.3
/usr/share/man/man3/PPI::Normal.3
/usr/share/man/man3/PPI::Normal::Standard.3
/usr/share/man/man3/PPI::Statement.3
/usr/share/man/man3/PPI::Statement::Break.3
/usr/share/man/man3/PPI::Statement::Compound.3
/usr/share/man/man3/PPI::Statement::Data.3
/usr/share/man/man3/PPI::Statement::End.3
/usr/share/man/man3/PPI::Statement::Expression.3
/usr/share/man/man3/PPI::Statement::Given.3
/usr/share/man/man3/PPI::Statement::Include.3
/usr/share/man/man3/PPI::Statement::Include::Perl6.3
/usr/share/man/man3/PPI::Statement::Null.3
/usr/share/man/man3/PPI::Statement::Package.3
/usr/share/man/man3/PPI::Statement::Scheduled.3
/usr/share/man/man3/PPI::Statement::Sub.3
/usr/share/man/man3/PPI::Statement::Unknown.3
/usr/share/man/man3/PPI::Statement::UnmatchedBrace.3
/usr/share/man/man3/PPI::Statement::Variable.3
/usr/share/man/man3/PPI::Statement::When.3
/usr/share/man/man3/PPI::Structure.3
/usr/share/man/man3/PPI::Structure::Block.3
/usr/share/man/man3/PPI::Structure::Condition.3
/usr/share/man/man3/PPI::Structure::Constructor.3
/usr/share/man/man3/PPI::Structure::For.3
/usr/share/man/man3/PPI::Structure::Given.3
/usr/share/man/man3/PPI::Structure::List.3
/usr/share/man/man3/PPI::Structure::Subscript.3
/usr/share/man/man3/PPI::Structure::Unknown.3
/usr/share/man/man3/PPI::Structure::When.3
/usr/share/man/man3/PPI::Token.3
/usr/share/man/man3/PPI::Token::ArrayIndex.3
/usr/share/man/man3/PPI::Token::Attribute.3
/usr/share/man/man3/PPI::Token::BOM.3
/usr/share/man/man3/PPI::Token::Cast.3
/usr/share/man/man3/PPI::Token::Comment.3
/usr/share/man/man3/PPI::Token::DashedWord.3
/usr/share/man/man3/PPI::Token::Data.3
/usr/share/man/man3/PPI::Token::End.3
/usr/share/man/man3/PPI::Token::HereDoc.3
/usr/share/man/man3/PPI::Token::Label.3
/usr/share/man/man3/PPI::Token::Magic.3
/usr/share/man/man3/PPI::Token::Number.3
/usr/share/man/man3/PPI::Token::Number::Binary.3
/usr/share/man/man3/PPI::Token::Number::Exp.3
/usr/share/man/man3/PPI::Token::Number::Float.3
/usr/share/man/man3/PPI::Token::Number::Hex.3
/usr/share/man/man3/PPI::Token::Number::Octal.3
/usr/share/man/man3/PPI::Token::Number::Version.3
/usr/share/man/man3/PPI::Token::Operator.3
/usr/share/man/man3/PPI::Token::Pod.3
/usr/share/man/man3/PPI::Token::Prototype.3
/usr/share/man/man3/PPI::Token::Quote.3
/usr/share/man/man3/PPI::Token::Quote::Double.3
/usr/share/man/man3/PPI::Token::Quote::Interpolate.3
/usr/share/man/man3/PPI::Token::Quote::Literal.3
/usr/share/man/man3/PPI::Token::Quote::Single.3
/usr/share/man/man3/PPI::Token::QuoteLike.3
/usr/share/man/man3/PPI::Token::QuoteLike::Backtick.3
/usr/share/man/man3/PPI::Token::QuoteLike::Command.3
/usr/share/man/man3/PPI::Token::QuoteLike::Readline.3
/usr/share/man/man3/PPI::Token::QuoteLike::Regexp.3
/usr/share/man/man3/PPI::Token::QuoteLike::Words.3
/usr/share/man/man3/PPI::Token::Regexp.3
/usr/share/man/man3/PPI::Token::Regexp::Match.3
/usr/share/man/man3/PPI::Token::Regexp::Substitute.3
/usr/share/man/man3/PPI::Token::Regexp::Transliterate.3
/usr/share/man/man3/PPI::Token::Separator.3
/usr/share/man/man3/PPI::Token::Structure.3
/usr/share/man/man3/PPI::Token::Symbol.3
/usr/share/man/man3/PPI::Token::Unknown.3
/usr/share/man/man3/PPI::Token::Whitespace.3
/usr/share/man/man3/PPI::Token::Word.3
/usr/share/man/man3/PPI::Token::_QuoteEngine.3
/usr/share/man/man3/PPI::Token::_QuoteEngine::Full.3
/usr/share/man/man3/PPI::Token::_QuoteEngine::Simple.3
/usr/share/man/man3/PPI::Tokenizer.3
/usr/share/man/man3/PPI::Transform.3
/usr/share/man/man3/PPI::Transform::UpdateCopyright.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/PPI.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Cache.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Document.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Document/File.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Document/Fragment.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Document/Normalized.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Dumper.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Element.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Exception.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Exception/ParserRejection.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Find.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Lexer.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Node.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Normal.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Normal/Standard.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Singletons.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Statement.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Statement/Break.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Statement/Compound.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Statement/Data.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Statement/End.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Statement/Expression.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Statement/Given.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Statement/Include.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Statement/Include/Perl6.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Statement/Null.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Statement/Package.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Statement/Scheduled.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Statement/Sub.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Statement/Unknown.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Statement/UnmatchedBrace.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Statement/Variable.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Statement/When.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Structure.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Structure/Block.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Structure/Condition.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Structure/Constructor.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Structure/For.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Structure/Given.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Structure/List.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Structure/Subscript.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Structure/Unknown.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Structure/When.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/ArrayIndex.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Attribute.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/BOM.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Cast.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Comment.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/DashedWord.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Data.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/End.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/HereDoc.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Label.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Magic.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Number.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Number/Binary.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Number/Exp.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Number/Float.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Number/Hex.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Number/Octal.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Number/Version.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Operator.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Pod.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Prototype.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Quote.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Quote/Double.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Quote/Interpolate.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Quote/Literal.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Quote/Single.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/QuoteLike.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/QuoteLike/Backtick.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/QuoteLike/Command.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/QuoteLike/Readline.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/QuoteLike/Regexp.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/QuoteLike/Words.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Regexp.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Regexp/Match.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Regexp/Substitute.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Regexp/Transliterate.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Separator.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Structure.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Symbol.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Unknown.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Whitespace.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/Word.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/_QuoteEngine.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/_QuoteEngine/Full.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Token/_QuoteEngine/Simple.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Tokenizer.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Transform.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Transform/UpdateCopyright.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/Util.pm
/usr/lib/perl5/vendor_perl/5.34.0/PPI/XSAccessor.pm
