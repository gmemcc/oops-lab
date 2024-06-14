import {ActionType, BetaSchemaForm, PageContainer, ProFormInstance, ProTable} from '@ant-design/pro-components';
import {queryApiReportsQueryPost} from "@/services/lab/queryApiReportsQueryPost";
import {FC, useRef, useState} from 'react';
import {Button} from "antd";
import {ProForm} from "@ant-design/pro-form/lib";
import {createApiReportsPost} from "@/services/lab/createApiReportsPost";

const Reports: FC = () => {
  const columns = [
    {
      title: '报告人',
      dataIndex: 'reporter',
      valueType: 'text',
    },
    {
      title: '报告日期',
      dataIndex: 'reportTime',
      valueType: 'dateTime',
    },
    {
      title: '工作内容',
      dataIndex: 'workContent',
      valueType: 'textarea',
      hideInSearch: true,
    },
    {
      title: '重点事件',
      dataIndex: 'concernedIncs',
      valueType: 'textarea',
      hideInSearch: true,
    }
  ] as any[];

  const tableActionRef = useRef<ActionType>();
  const formRef = useRef<ProFormInstance>();
  const [formVisible, setFormVisible] = useState(false);
  const [report, setReport] = useState<any>();

  return (
      <PageContainer>
        <ProTable
            columns={columns}
            actionRef={tableActionRef}
            request={async (params) => {
              return queryApiReportsQueryPost({
                reporter: params.reporter,
                report_time: params.reportTime,
              });
            }}
            toolBarRender={() => [
              <Button
                  key="add"
                  type="primary"
                  onClick={() => {
                    formRef.current?.resetFields();
                    setReport(undefined);
                    setFormVisible(true);
                  }}
              >
                创建周报
              </Button>,
            ]}
            pagination={{
              pageSize: 10,
            }}
            options={{
              fullScreen: true,
            }}
            defaultSize={'small'}
        />
        <BetaSchemaForm
            title={report ? '编辑周报' : '创建周报'}
            layoutType={'DrawerForm'}
            columns={columns}
            formRef={formRef}
            visible={formVisible}
            onFinish={async (values) => {
              await createApiReportsPost(values);
              setFormVisible(false);
              tableActionRef.current?.reload();
            }}
        />
      </PageContainer>
  );
};

export default Reports;
