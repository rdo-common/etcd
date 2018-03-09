# http://github.com/coreos/etcd
%global goipath         github.com/coreos/etcd
%global gcommit         121edf0467052d55876a817b89875fb39a99bf78

%gometa -i

%global man_version     3.2.16

Name:           etcd
Version:	3.2.16
Release:	1%{?dist}
Summary:	A highly-available key value store for shared configuration
License:	ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:	%{name}.service
Source2:	%{name}.conf
Source3:        man-%{man_version}.tar.gz

Patch0:         Fix-format-errors.patch

BuildRequires: golang(github.com/bgentry/speakeasy)
BuildRequires: golang(github.com/boltdb/bolt)
BuildRequires: golang(github.com/cheggaaa/pb)
BuildRequires: golang(github.com/cockroachdb/cmux)
BuildRequires: golang(github.com/coreos/go-semver/semver)
BuildRequires: golang(github.com/coreos/go-systemd/daemon)
BuildRequires: golang(github.com/coreos/go-systemd/util)
BuildRequires: golang(github.com/coreos/pkg/capnslog)
BuildRequires: golang(github.com/dgrijalva/jwt-go)
BuildRequires: golang(github.com/dustin/go-humanize)
BuildRequires: golang(github.com/ghodss/yaml)
BuildRequires: golang(github.com/gogo/protobuf/proto)
BuildRequires: golang(github.com/golang/groupcache/lru)
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/google/btree)
BuildRequires: golang(github.com/grpc-ecosystem/go-grpc-prometheus)
BuildRequires: golang(github.com/grpc-ecosystem/grpc-gateway/runtime)
BuildRequires: golang(github.com/grpc-ecosystem/grpc-gateway/utilities)
BuildRequires: golang(github.com/jonboulle/clockwork)
BuildRequires: golang(github.com/kr/pty)
BuildRequires: golang(github.com/olekukonko/tablewriter)
BuildRequires: golang(github.com/prometheus/client_golang/prometheus)
BuildRequires: golang(github.com/spf13/cobra)
BuildRequires: golang(github.com/spf13/pflag)
BuildRequires: golang(github.com/ugorji/go/codec)
BuildRequires: golang(github.com/urfave/cli)
BuildRequires: golang(github.com/xiang90/probing)
BuildRequires: golang(golang.org/x/crypto/bcrypt)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/net/http2)
BuildRequires: golang(golang.org/x/net/trace)
BuildRequires: golang(golang.org/x/time/rate)
BuildRequires: golang(google.golang.org/grpc)
BuildRequires: golang(google.golang.org/grpc/codes)
BuildRequires: golang(google.golang.org/grpc/credentials)
BuildRequires: golang(google.golang.org/grpc/grpclog)
BuildRequires: golang(google.golang.org/grpc/metadata)
BuildRequires: golang(google.golang.org/grpc/naming)
BuildRequires: golang(google.golang.org/grpc/peer)
BuildRequires: golang(google.golang.org/grpc/transport)

BuildRequires:	systemd

%description
A highly-available key value store for shared configuration.

%package devel
Summary:        etcd golang devel libraries
BuildArch:      noarch

BuildRequires: golang(github.com/bgentry/speakeasy)
BuildRequires: golang(github.com/cheggaaa/pb)
BuildRequires: golang(github.com/cockroachdb/cmux)
BuildRequires: golang(github.com/coreos/bbolt)
BuildRequires: golang(github.com/coreos/go-semver/semver)
BuildRequires: golang(github.com/coreos/go-systemd/daemon)
BuildRequires: golang(github.com/coreos/go-systemd/util)
BuildRequires: golang(github.com/coreos/pkg/capnslog)
BuildRequires: golang(github.com/dgrijalva/jwt-go)
BuildRequires: golang(github.com/dustin/go-humanize)
BuildRequires: golang(github.com/ghodss/yaml)
BuildRequires: golang(github.com/gogo/protobuf/proto)
BuildRequires: golang(github.com/golang/groupcache/lru)
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/google/btree)
BuildRequires: golang(github.com/grpc-ecosystem/go-grpc-prometheus)
BuildRequires: golang(github.com/grpc-ecosystem/grpc-gateway/runtime)
BuildRequires: golang(github.com/grpc-ecosystem/grpc-gateway/utilities)
BuildRequires: golang(github.com/jonboulle/clockwork)
BuildRequires: golang(github.com/kr/pty)
BuildRequires: golang(github.com/olekukonko/tablewriter)
BuildRequires: golang(github.com/prometheus/client_golang/prometheus)
BuildRequires: golang(github.com/spf13/cobra)
BuildRequires: golang(github.com/spf13/pflag)
BuildRequires: golang(github.com/ugorji/go/codec)
BuildRequires: golang(github.com/urfave/cli)
BuildRequires: golang(github.com/xiang90/probing)
BuildRequires: golang(golang.org/x/crypto/bcrypt)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/net/http2)
BuildRequires: golang(golang.org/x/net/trace)
BuildRequires: golang(golang.org/x/time/rate)
BuildRequires: golang(google.golang.org/genproto/googleapis/api/annotations)
BuildRequires: golang(google.golang.org/grpc)
BuildRequires: golang(google.golang.org/grpc/codes)
BuildRequires: golang(google.golang.org/grpc/credentials)
BuildRequires: golang(google.golang.org/grpc/grpclog)
BuildRequires: golang(google.golang.org/grpc/health/grpc_health_v1)
BuildRequires: golang(google.golang.org/grpc/keepalive)
BuildRequires: golang(google.golang.org/grpc/metadata)
BuildRequires: golang(google.golang.org/grpc/naming)
BuildRequires: golang(google.golang.org/grpc/peer)
BuildRequires: golang(google.golang.org/grpc/status)

%description devel
golang development libraries for etcd, a highly-available key value store for
shared configuration.

%prep
%setup -q -n man-%{man_version} -T -b 3
%gosetup -q
%patch0 -p1

mkdir -p man/man1
cp ../man-%{man_version}/*.1 man/man1/.

sed -i 's/"gopkg\.in\/cheggaaa\/pb\.v1/"github\.com\/cheggaaa\/pb/g' $(find . -name '*.go')
#"

%build
%gobuildroot

%gobuild -o _bin/etcd    %{goipath}/cmd/etcd
%gobuild -o _bin/etcdctl %{goipath}/cmd/etcdctl

%install
install -D -p -m 0755 _bin/%{name} %{buildroot}%{_bindir}/%{name}
install -D -p -m 0755 _bin/%{name}ctl %{buildroot}%{_bindir}/%{name}ctl
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}
install -m 644 -t %{buildroot}%{_sysconfdir}/%{name} %{SOURCE2}

# install manpages
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 man/man1/* %{buildroot}%{_mandir}/man1

# And create /var/lib/etcd
install -d -m 0755 %{buildroot}%{_sharedstatedir}/%{name}

# source codes for building projects
%goinstall integration/fixtures etcdserver/api/v2http/testdata

%check
# tools/functional-tester/etcd-agent expects etcd binary at GOPATH/bin/etcd
%gochecks -d clientv3 -d e2e -d tools/functional-tester/etcd-agent -d integration -d clientv3/integration

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc *.md
%config(noreplace) %{_sysconfdir}/%{name}
%{_bindir}/%{name}
%{_bindir}/%{name}ctl
%dir %attr(-,%{name},%{name}) %{_sharedstatedir}/%{name}
%{_unitdir}/%{name}.service
%{_mandir}/man1/*.1*

%files devel -f devel.file-list
%license LICENSE
%doc *.md
%doc glide.lock

%changelog
* Fri Mar 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 3.2.16-1.git121edf0
- Update to 3.2.16

* Tue Mar 06 2018 Jan Chaloupka <jchaloup@redhat.com> - 3.2.7-5.gitbb66589
- Update to spec 3.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Jan Chaloupka <jchaloup@redhat.com> - 3.2.7-3
- Polish the spec file

* Tue Nov 07 2017 Jan Chaloupka <jchaloup@redhat.com> - 3.2.7-2
- Generate man pages

* Sun Sep 24 2017 Jan Chaloupka <jchaloup@redhat.com> - 3.2.7-1
- Update to 3.2.7
  related: #1448611

* Tue Aug 15 2017 Jan Chaloupka <jchaloup@redhat.com> - 3.2.5-1
- Update to 3.2.5
  resolves: #1448611

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 11 2017 Jan Chaloupka <jchaloup@redhat.com> - 3.1.9-1
- Update to 3.1.9
  resolves: #1460496

* Mon Jun 05 2017 Jan Chaloupka <jchaloup@redhat.com> - 3.1.8-1
  Update to 3.1.8
  resolves: #1458717

* Tue May 02 2017 Jan Chaloupka <jchaloup@redhat.com> - 3.1.7-1
- Update to 3.1.7
  resolves: #1447232

* Thu Apr 20 2017 Jan Chaloupka <jchaloup@redhat.com> - 3.1.6-1
- Update to 3.1.6
  resolves: #1444068

* Tue Mar 28 2017 Jan Chaloupka <jchaloup@redhat.com> - 3.1.5-1
- Update to 3.1.5
  resolves: #1436452

* Mon Mar 27 2017 Jan Chaloupka <jchaloup@redhat.com> - 3.1.4-1
- Update to 3.1.4
  resolves: #1435028

* Mon Mar 20 2017 Jan Chaloupka <jchaloup@redhat.com> - 3.1.3-1
- Update to v3.1.3
  related: #1415341

* Tue Mar 14 2017 Jan Chaloupka <jchaloup@redhat.com> - 3.1.0-1
- Update to v3.1.0
  related: #1415341

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Jan Chaloupka <jchaloup@redhat.com> - 3.0.17-1
- Update to v3.0.17
  etcd-top removed by upstream
  resolves: #1415622

* Fri Nov 18 2016 jchaloup <jchaloup@redhat.com> - 3.0.15-2
- Remove ppc64le architecture restriction
  resolves: #1396463

* Tue Nov 15 2016 jchaloup <jchaloup@redhat.com> - 3.0.15-1
- Update to v3.0.15
  related: #1382965

* Mon Nov 07 2016 jchaloup <jchaloup@redhat.com> - 3.0.14-1
- Update to v3.0.14
  related: #1382965

* Thu Oct 27 2016 jchaloup <jchaloup@redhat.com> - 3.0.13-1
- Update to v3.0.13
  related: #1382965

* Mon Oct 24 2016 jchaloup <jchaloup@redhat.com> - 3.0.12-2
- Extend supported architectures with s390x

* Thu Oct 13 2016 jchaloup <jchaloup@redhat.com> - 3.0.12-1
- Update to v3.0.12
  related: #1382965

* Fri Sep 16 2016 jchaloup <jchaloup@redhat.com> - 3.0.9-1
- Update to v3.0.9
  related: #1374880

* Wed Sep 14 2016 jchaloup <jchaloup@redhat.com> - 3.0.8-1
- Update to v3.0.8
  resolves: #1374880

* Fri Sep 09 2016 jchaloup <jchaloup@redhat.com> - 3.0.7-1
- Update to v3.0.7
  resolves: #1370678

* Tue Aug 16 2016 jchaloup <jchaloup@redhat.com> - 3.0.4-2
- Hack test to provide ability to run unit-tests and integration tests
  Still, keeping it disabled by default as it keeps failing
  related: #1351818

* Tue Aug 02 2016 jchaloup <jchaloup@redhat.com> - 3.0.4-1
- Update to 3.0.4
  related: #1351818

* Thu Jul 28 2016 jchaloup <jchaloup@redhat.com> - 3.0.2-1
- Update to 3.0.2
  resolves: #1351818

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-0.2.beta0
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sun May 15 2016 jchaloup <jchaloup@redhat.com> - 3.0.0-0.1.beta0
- Update to v3.0.0-beta0 (build from bundled until new deps appear in dist-git)
  resolves: #1333988

* Sat Apr 30 2016 jchaloup <jchaloup@redhat.com> - 2.3.3-1
- Update to v2.3.3
  resolves: #1331896

* Fri Apr 22 2016 jchaloup <jchaloup@redhat.com> - 2.3.2-1
- Update to v2.3.2
  resolves: #1329438

* Sat Apr  9 2016 Peter Robinson <pbrobinson@fedoraproject.org> 2.3.1-3
- Enable aarch64

* Wed Apr 06 2016 jchaloup <jchaloup@redhat.com> - 2.3.1-2
- Don't apply patch (for tests only which are disabled atm)

* Mon Apr 04 2016 jchaloup <jchaloup@redhat.com> - 2.3.1-1
- Update to v.2.3.1
  resolves: #1323375

* Sun Mar 20 2016 jchaloup <jchaloup@redhat.com> - 2.3.0-1
- Update to v2.3.0
  resolves: #1314441

* Wed Mar 09 2016 jchaloup <jchaloup@redhat.com> - 2.2.5-4
- Only ppc64le is supported, ppc64 not
  related: #1315419

* Tue Mar 08 2016 jchaloup <jchaloup@redhat.com> - 2.2.5-3
- Extend archs to all supported
  resolves: #1315419

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-2
- https://fedoraproject.org/wiki/Changes/golang1.6

* Thu Feb 18 2016 jchaloup <jchaloup@redhat.com> - 2.2.5-1
- Update to v2.2.5

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 jchaloup <jchaloup@redhat.com> - 2.2.4-1
- Update to v2.2.4
  resolves: #1300558

* Fri Jan 08 2016 jchaloup <jchaloup@redhat.com> - 2.2.3-1
- Update to v2.2.3
  resolves: #1296809

* Tue Dec 29 2015 jchaloup <jchaloup@redhat.com> - 2.2.2-2
- add missing options to etcd help (thanks to Joy Pu ypu@redhat.com)
- add more information when running etcd as a service

* Mon Dec 07 2015 jchaloup <jchaloup@redhat.com> - 2.2.2-1
- Update to v2.2.2

* Mon Nov 16 2015 jchaloup <jchaloup@redhat.com> - 2.2.1-4
- Update etcd.conf: add new options, fix current

* Fri Oct 30 2015 jchaloup <jchaloup@redhat.com> - 2.2.1-3
- Add After=network-online.target and Wants=network-online.target
  to etcd.service

* Tue Oct 20 2015 jchaloup <jchaloup@redhat.com> - 2.2.1-2
- Set Type=notify instead of simple in etcd.service (upstream #1576)
  related: #1272438

* Fri Oct 16 2015 jchaloup <jchaloup@redhat.com> - 2.2.1-1
- Update to v2.2.1
  resolves: #1272438

* Fri Sep 11 2015 jchaloup <jchaloup@redhat.com> - 2.2.0-1
- Update to v2.2.0 (etcd-migrate gone)
- Update to spec-2.1
  resolves: #1253864

* Mon Aug 31 2015 jchaloup <jchaloup@redhat.com> - 2.1.2-1
- Update to v2.1.2
  resolves: #1258599

* Thu Jul 30 2015 jchaloup <jchaloup@redhat.com> - 2.1.1-2
- Enable debug info again
  related: #1214958

* Mon Jul 20 2015 jchaloup <jchaloup@redhat.com> - 2.1.1-1
- fix definition of GOPATH for go1.5
- fix definition of gobuild function for non-debug way
- Update to v2.1.1
  resolves: #1214958

* Fri Jul 10 2015 jchaloup <jchaloup@redhat.com> - 2.0.13-3
- set GOMAXPROCS to use all processors available

* Mon Jun 29 2015 jchaloup <jchaloup@redhat.com> - 2.0.13-2
- Remove -s option from -ldflags string as it removes symbol table
  'go tool l6' gives explanation of all available options
  resolves: #1236320

* Fri Jun 26 2015 jchaloup <jchaloup@redhat.com> - 2.0.13-1
- Update to v2.0.13

* Thu Jun 25 2015 jchaloup <jchaloup@redhat.com> - 2.0.12-2
- Add restart policy and set LimitNOFILE to/in etcd.service file
- Update etcd.config file: add new flags and remove depricated
- Update 'go build' flags for GIT_SHA (used in build script)
- Don't use 4001 and 7001 ports in etcd.conf, they are replaced with 2379 and 2380

* Wed Jun 24 2015 jchaloup <jchaloup@redhat.com> - 2.0.12-1
- Update to v2.0.12
- Polish spec file

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 jchaloup <jchaloup@redhat.com> - 2.0.11-2
- ETCD_ADVERTISE_CLIENT_URLS has to be set if ETCD_LISTEN_CLIENT_URLS is
  related: #1222416

* Mon May 18 2015 jchaloup <jchaloup@redhat.com> - 2.0.11-1
- Update to v2.0.11
  resolves: #1222416

* Thu Apr 23 2015 jchaloup <jchaloup@redhat.com> - 2.0.10-1
- Update to v2.0.10
  resolves: #1214705

* Wed Apr 08 2015 jchaloup <jchaloup@redhat.com> - 2.0.9-1
- Update to v2.0.9
  resolves: #1209666

* Fri Apr 03 2015 jchaloup <jchaloup@redhat.com> - 2.0.8-0.2
- Update spec file to fit for rhel too (thanks to eparis)
  related: #1207881

* Wed Apr 01 2015 jchaloup <jchaloup@redhat.com> - 2.0.8-0.1
- Update to v2.0.8
  resolves: #1207881

* Tue Mar 31 2015 jchaloup <jchaloup@redhat.com> - 2.0.7-0.1
- Update to v2.0.7
  Add Godeps.json to doc
  related: #1191441

* Thu Mar 12 2015 jchaloup <jchaloup@redhat.com> - 2.0.5-0.1
- Bump to 9481945228b97c5d019596b921d8b03833964d9e (v2.0.5)

* Tue Mar 10 2015 Eric Paris <eparis@redhat.com> - 2.0.3-0.2
- Fix .service files to work if no config file

* Fri Feb 20 2015 jchaloup <jchaloup@redhat.com> - 2.0.3-0.1
- Bump to upstream 4d728cc8c488a545a8bdeafd054d9ccc2bfb6876

* Wed Feb 18 2015 jchaloup <jchaloup@redhat.com> - 2.0.1-0.2
- Update configuration and service file
  Fix depricated ErrWrongType after update of gogo/protobuf
  related: #1191441

* Wed Feb 11 2015 jchaloup <jchaloup@redhat.com> - 2.0.1-0.1
- Update to 2.0.1
  resolves: #1191441

* Mon Feb 09 2015 jchaloup <jchaloup@redhat.com> - 2.0.0-0.5
- Add missing debug info to binaries (patch from Jan Kratochvil)
  resolves: #1184257

* Fri Jan 30 2015 jchaloup <jchaloup@redhat.com> - 2.0.0-0.4
- Update to etcd-2.0.0
- use gopath as the last directory to search for source code
  related: #1176138

* Mon Jan 26 2015 jchaloup <jchaloup@redhat.com> - 2.0.0-0.3.rc1
- default to /var/lib/etcd/default.etcd as 2.0 uses that default (f21 commit byt eparis)
  related: #1176138
  fix /etc/etcd/etcd.conf path

* Tue Jan 20 2015 jchaloup <jchaloup@redhat.com> - 2.0.0-0.2.rc1
- Update of BuildRequires/Requires, Provides and test
  Add BuildRequire on jonboulle/clockwork
  related: #1176138

* Tue Dec 23 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2.0.0-0.1.rc1
- Resolves: rhbz#1176138 - update to v2.0.0-rc1
- do not redefine gopath
- use jonboulle/clockwork from within Godeps

* Fri Oct 17 2014 jchaloup <jchaloup@redhat.com> - 0.4.6-7
- Add ExclusiveArch for go_arches

* Mon Oct 06 2014 jchaloup <jchaloup@redhat.com> - 0.4.6-6
- related: #1047194
  Remove dependency on go.net

* Mon Oct 06 2014 jchaloup <jchaloup@redhat.com> - 0.4.6-5
- Fix the .service file so it can launch!
  related: #1047194

* Mon Sep 22 2014 jchaloup <jchaloup@redhat.com> - 0.4.6-4
- resolves: #1047194
  Update to 0.4.6 from https://github.com/projectatomic/etcd-package

* Tue Aug 19 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.4.6-3
- Add devel sub-package

* Wed Aug 13 2014 Eric Paris <eparis@redhat.com> - 0.4.6-2
- Bump to 0.4.6
- run as etcd, not root

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Oct 20 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.1.2-5
- goprotobuf library unbundled (see rhbz #1018477)
- go-log library unbundled (see rhbz #1018478)
- go-raft library unbundled (see rhbz #1018479)
- go-systemd library unbundled (see rhbz #1018480)
- kardianos library unbundled (see rhbz #1018481)

* Sun Oct 13 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.1.2-4
- go.net library unbundled (see rhbz #1018476)

* Sat Oct 12 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.1.2-3
- Prepare for packages unbundling
- Verbose build

* Sat Oct 12 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.1.2-2
- Fix typo in the etc.service file

* Sat Oct 12 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.1.2-1
- Ver. 0.1.2
- Integrate with systemd

* Mon Aug 26 2013 Luke Cypret <cypret@fedoraproject.org> - 0.1.1-1
- Initial creation
