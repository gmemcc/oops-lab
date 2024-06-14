import { ProLayoutProps } from '@ant-design/pro-components';

const Settings: ProLayoutProps & {
  pwa?: boolean;
  logo?: string;
} = {
  layout: 'mix',
  contentWidth: 'Fluid',
  fixedHeader: false,
  fixSiderbar: true,
  colorWeak: false,
  title: 'OverseasOps Lab',
  pwa: true,
  logo: '/logo-full-dark.svg',
  headerTitleRender: (logo, _, props) => {
    let width = "auto";
    let height = "auto";
    // @ts-ignore
    let logoProps = logo?.props;
    if (logoProps) {
      width = logoProps.width;
      height = logoProps.height;
    }
    return props.navTheme === 'light' ? <img src="/logo-full.svg"  width={width}height={height} /> : logo;
  },
};

export default Settings;
