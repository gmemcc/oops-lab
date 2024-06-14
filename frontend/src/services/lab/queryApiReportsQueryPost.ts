// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

/** Query POST /api/reports/query */
export async function queryApiReportsQueryPost(
  // 叠加生成的Param类型 (非body参数swagger默认没有生成对象)
  params: API.queryApiReportsQueryPostParams,
  options?: { [key: string]: any },
) {
  return request<API.PageReportModel_>('/api/reports/query', {
    method: 'POST',
    params: {
      ...params,
    },
    ...(options || {}),
  });
}
