import Guide from '@/components/Guide';
import {trim} from '@/utils/format';
import {PageContainer} from '@ant-design/pro-components';
import {useModel} from '@umijs/max';

const HomePage: React.FC = () => {
  const {name} = useModel('global');
  return (
      <PageContainer ghost>
        <Guide name={trim(name)}/>
      </PageContainer>
  );
};

export default HomePage;
