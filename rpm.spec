Name:       azure_metrics_exporter
Summary:    Most simple RPM package
Version:    1
Release:    1
License:    BEDE


%description
azure_metrics_exporter

%prep
# we have no source, so nothing here

%build

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 %{_topdir}/azure_metrics_exporter %{buildroot}/usr/bin/azure-metrics-exporter

%files
/usr/bin/azure_metrics_exporter

%changelog
# let skip this for now
