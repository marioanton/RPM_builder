Name:       azure_metrics_exporter
Version:    1
Release:    1
Summary:    Most simple RPM package
License:    FIXME

%description
This is my first RPM package, which does nothing.

%prep
# we have no source, so nothing here

%build

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 azure_metrics_exporter %{buildroot}/usr/bin/azure_metrics_exporter

%files
/usr/bin/azure_metrics_exporter

%changelog
# let skip this for now
