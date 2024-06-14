// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

/** Update PUT /api/reports/${param0} */
export async function updateApiReportsIdPut(
  // 叠加生成的Param类型 (非body参数swagger默认没有生成对象)
  params: API.updateApiReportsIdPutParams,
  body: API.ReportModel,
  options?: { [key: string]: any },
) {
  const { id: param0, ...queryParams } = params;
  return request<API.ReportModel>(`/api/reports/${param0}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    params: { ...queryParams },
    data: body,
    ...(options || {}),
  });
}
