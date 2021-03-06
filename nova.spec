#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x4F398DEAE440091C (infra-root@openstack.org)
#
Name     : nova
Version  : 19.1.0
Release  : 171
URL      : https://tarballs.openstack.org/nova/nova-19.1.0.tar.gz
Source0  : https://tarballs.openstack.org/nova/nova-19.1.0.tar.gz
Source1  : nova.tmpfiles
Source2  : https://tarballs.openstack.org/nova/nova-19.1.0.tar.gz.asc
Summary  : Cloud computing fabric controller
Group    : Development/Tools
License  : Apache-2.0
Requires: nova-bin = %{version}-%{release}
Requires: nova-config = %{version}-%{release}
Requires: nova-data = %{version}-%{release}
Requires: nova-license = %{version}-%{release}
Requires: nova-python = %{version}-%{release}
Requires: nova-python3 = %{version}-%{release}
Requires: Babel
Requires: Jinja2
Requires: Paste
Requires: PasteDeploy
Requires: Routes
Requires: SQLAlchemy
Requires: WebOb
Requires: castellan
Requires: cryptography
Requires: cursive
Requires: decorator
Requires: eventlet
Requires: futurist
Requires: greenlet
Requires: iso8601
Requires: jsonschema
Requires: keystoneauth1
Requires: keystonemiddleware
Requires: lxml
Requires: microversion_parse
Requires: netaddr
Requires: netifaces
Requires: os-brick
Requires: os-resource-classes
Requires: os-service-types
Requires: os-traits
Requires: os-win
Requires: os-xenapi
Requires: os_vif
Requires: oslo.cache
Requires: oslo.concurrency
Requires: oslo.config
Requires: oslo.context
Requires: oslo.db
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.messaging
Requires: oslo.middleware
Requires: oslo.policy
Requires: oslo.privsep
Requires: oslo.reports
Requires: oslo.rootwrap
Requires: oslo.serialization
Requires: oslo.service
Requires: oslo.upgradecheck
Requires: oslo.utils
Requires: oslo.versionedobjects
Requires: osprofiler
Requires: paramiko
Requires: pbr
Requires: prettytable
Requires: psutil
Requires: pypowervm
Requires: python-cinderclient
Requires: python-dateutil
Requires: python-glanceclient
Requires: python-neutronclient
Requires: requests
Requires: retrying
Requires: rfc3986
Requires: setuptools
Requires: six
Requires: sqlalchemy-migrate
Requires: stevedore
Requires: taskflow
Requires: tooz
Requires: websockify
Requires: zVMCloudConnector
BuildRequires : Babel
BuildRequires : Jinja2
BuildRequires : Paste
BuildRequires : PasteDeploy
BuildRequires : Routes
BuildRequires : SQLAlchemy
BuildRequires : WebOb
BuildRequires : buildreq-distutils3
BuildRequires : castellan
BuildRequires : cryptography
BuildRequires : cursive
BuildRequires : decorator
BuildRequires : eventlet
BuildRequires : futurist
BuildRequires : greenlet
BuildRequires : iso8601
BuildRequires : jsonschema
BuildRequires : keystoneauth1
BuildRequires : keystonemiddleware
BuildRequires : lxml
BuildRequires : microversion_parse
BuildRequires : netaddr
BuildRequires : netifaces
BuildRequires : os-brick
BuildRequires : os-resource-classes
BuildRequires : os-service-types
BuildRequires : os-traits
BuildRequires : os-win
BuildRequires : os-xenapi
BuildRequires : os_vif
BuildRequires : oslo.cache
BuildRequires : oslo.concurrency
BuildRequires : oslo.config
BuildRequires : oslo.context
BuildRequires : oslo.db
BuildRequires : oslo.i18n
BuildRequires : oslo.log
BuildRequires : oslo.messaging
BuildRequires : oslo.middleware
BuildRequires : oslo.policy
BuildRequires : oslo.privsep
BuildRequires : oslo.reports
BuildRequires : oslo.rootwrap
BuildRequires : oslo.serialization
BuildRequires : oslo.service
BuildRequires : oslo.upgradecheck
BuildRequires : oslo.utils
BuildRequires : oslo.versionedobjects
BuildRequires : osprofiler
BuildRequires : paramiko
BuildRequires : pbr
BuildRequires : prettytable
BuildRequires : psutil
BuildRequires : pypowervm
BuildRequires : python-cinderclient
BuildRequires : python-dateutil
BuildRequires : python-glanceclient
BuildRequires : python-neutronclient
BuildRequires : requests
BuildRequires : retrying
BuildRequires : rfc3986
BuildRequires : setuptools
BuildRequires : six
BuildRequires : sqlalchemy-migrate
BuildRequires : stevedore
BuildRequires : taskflow
BuildRequires : tooz
BuildRequires : websockify
BuildRequires : zVMCloudConnector
Patch1: 0001-Unfreeze-jsonschema.patch

%description
Team and repository tags
        ========================

%package bin
Summary: bin components for the nova package.
Group: Binaries
Requires: nova-data = %{version}-%{release}
Requires: nova-config = %{version}-%{release}
Requires: nova-license = %{version}-%{release}

%description bin
bin components for the nova package.


%package config
Summary: config components for the nova package.
Group: Default

%description config
config components for the nova package.


%package data
Summary: data components for the nova package.
Group: Data

%description data
data components for the nova package.


%package license
Summary: license components for the nova package.
Group: Default

%description license
license components for the nova package.


%package python
Summary: python components for the nova package.
Group: Default
Requires: nova-python3 = %{version}-%{release}

%description python
python components for the nova package.


%package python3
Summary: python3 components for the nova package.
Group: Default
Requires: python3-core
Provides: pypi(nova)
Requires: pypi(babel)
Requires: pypi(castellan)
Requires: pypi(cryptography)
Requires: pypi(cursive)
Requires: pypi(decorator)
Requires: pypi(eventlet)
Requires: pypi(futurist)
Requires: pypi(greenlet)
Requires: pypi(iso8601)
Requires: pypi(jinja2)
Requires: pypi(jsonschema)
Requires: pypi(keystoneauth1)
Requires: pypi(keystonemiddleware)
Requires: pypi(lxml)
Requires: pypi(microversion_parse)
Requires: pypi(netaddr)
Requires: pypi(netifaces)
Requires: pypi(openstacksdk)
Requires: pypi(os_brick)
Requires: pypi(os_resource_classes)
Requires: pypi(os_service_types)
Requires: pypi(os_traits)
Requires: pypi(os_vif)
Requires: pypi(os_win)
Requires: pypi(os_xenapi)
Requires: pypi(oslo.cache)
Requires: pypi(oslo.concurrency)
Requires: pypi(oslo.config)
Requires: pypi(oslo.context)
Requires: pypi(oslo.db)
Requires: pypi(oslo.i18n)
Requires: pypi(oslo.log)
Requires: pypi(oslo.messaging)
Requires: pypi(oslo.middleware)
Requires: pypi(oslo.policy)
Requires: pypi(oslo.privsep)
Requires: pypi(oslo.reports)
Requires: pypi(oslo.rootwrap)
Requires: pypi(oslo.serialization)
Requires: pypi(oslo.service)
Requires: pypi(oslo.upgradecheck)
Requires: pypi(oslo.utils)
Requires: pypi(oslo.versionedobjects)
Requires: pypi(paramiko)
Requires: pypi(paste)
Requires: pypi(pastedeploy)
Requires: pypi(pbr)
Requires: pypi(prettytable)
Requires: pypi(psutil)
Requires: pypi(pypowervm)
Requires: pypi(python_cinderclient)
Requires: pypi(python_dateutil)
Requires: pypi(python_glanceclient)
Requires: pypi(python_neutronclient)
Requires: pypi(requests)
Requires: pypi(retrying)
Requires: pypi(rfc3986)
Requires: pypi(routes)
Requires: pypi(six)
Requires: pypi(sqlalchemy)
Requires: pypi(sqlalchemy_migrate)
Requires: pypi(stevedore)
Requires: pypi(taskflow)
Requires: pypi(tooz)
Requires: pypi(webob)
Requires: pypi(websockify)
Requires: pypi(zvmcloudconnector)

%description python3
python3 components for the nova package.


%prep
%setup -q -n nova-19.1.0
cd %{_builddir}/nova-19.1.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1584644413
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nova
cp %{_builddir}/nova-19.1.0/LICENSE %{buildroot}/usr/share/package-licenses/nova/294b43b2cec9919063be1a3b49e8722648424779
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/nova.conf
## install_append content
install -d -m 755 %{buildroot}/usr/share/defaults/nova
#install -p -D -m 644 etc/nova/*.conf %{buildroot}/usr/share/defaults/nova/
#install -p -D -m 644 etc/nova/*.ini %{buildroot}/usr/share/defaults/nova/
#install -p -D -m 644 etc/nova/*.json %{buildroot}/usr/share/defaults/nova/
mv %{buildroot}/usr/etc/nova/* %{buildroot}/usr/share/defaults/nova/
rm -rf %{buildroot}/usr/etc
#
#install -d -m 755 %{buildroot}/usr/share/defaults/nova/
#install -p -D -m 644 etc/nova/nova.conf.sample %{buildroot}/usr/share/defaults/nova/nova.conf
#install -p -D -m 644 etc/nova/nova-docker.conf.sample %{buildroot}/usr/share/defaults/nova/nova-docker.conf
#install -p -D -m 644 etc/nova/nova-lkvm.conf.sample %{buildroot}/usr/share/defaults/nova/nova-lkvm.conf
#
#install -d -m 755 %{buildroot}/usr/share/nova/rootwrap.d
##mv %{buildroot}/usr/share/defaults/nova/rootwrap.conf %{buildroot}/usr/share/nova/
#install -p -D -m 640 etc/nova/rootwrap.d/*.filters %{buildroot}/usr/share/nova/rootwrap.d/
#
#install -d -m 750 %{buildroot}/usr/share/defaults/sudo/sudoers.d
#install -p -D -m 440 etc/sudoers.d/nova.sudoers %{buildroot}/usr/share/defaults/sudo/sudoers.d/nova
#
#install -d -m 755 %{buildroot}/usr/lib/modules-load.d/
#install -p -D -m 640 nbd.conf %{buildroot}/usr/lib/modules-load.d/
#
#install -m 0755 -d %{buildroot}/usr/share/httpd/cgi-bin/nova
#cp nova/wsgi/*.py %{buildroot}/usr/share/httpd/cgi-bin/nova
#
#install -m 0755 -d %{buildroot}/usr/share/defaults/httpd/conf.d
##install -p -D -m 644 nova/wsgi/nova-api-metadata.httpd %{buildroot}/usr/share/defaults/httpd/conf.d/nova-api-metadata.conf
#install -p -D -m 644 nova/wsgi/nova-api.httpd  %{buildroot}/usr/share/defaults/httpd/conf.d/nova-api.template
#
#install -m 0755 -d %{buildroot}/usr/share/uwsgi/nova
#cp nova/wsgi/*.ini %{buildroot}/usr/share/uwsgi/nova
#
#install -m 0755 -d %{buildroot}/usr/share/nginx/conf.d
#install -p -D -m 644 nova/wsgi/nova-api-metadata.nginx %{buildroot}/usr/share/nginx/conf.d/nova-api-metadata.conf
#install -p -D -m 644 nova/wsgi/nova-api.nginx %{buildroot}/usr/share/nginx/conf.d/nova-api.template
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nova-api
/usr/bin/nova-api-metadata
/usr/bin/nova-api-os-compute
/usr/bin/nova-api-wsgi
/usr/bin/nova-cells
/usr/bin/nova-compute
/usr/bin/nova-conductor
/usr/bin/nova-console
/usr/bin/nova-consoleauth
/usr/bin/nova-dhcpbridge
/usr/bin/nova-manage
/usr/bin/nova-metadata-wsgi
/usr/bin/nova-network
/usr/bin/nova-novncproxy
/usr/bin/nova-placement-api
/usr/bin/nova-policy
/usr/bin/nova-rootwrap
/usr/bin/nova-rootwrap-daemon
/usr/bin/nova-scheduler
/usr/bin/nova-serialproxy
/usr/bin/nova-spicehtml5proxy
/usr/bin/nova-status
/usr/bin/nova-xvpvncproxy

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/nova.conf

%files data
%defattr(-,root,root,-)
/usr/share/defaults/nova/api-paste.ini
/usr/share/defaults/nova/rootwrap.conf
/usr/share/defaults/nova/rootwrap.d/api-metadata.filters
/usr/share/defaults/nova/rootwrap.d/compute.filters
/usr/share/defaults/nova/rootwrap.d/network.filters

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nova/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
