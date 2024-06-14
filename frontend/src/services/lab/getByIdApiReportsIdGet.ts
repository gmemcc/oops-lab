// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

/** Get By Id GET /api/reports/${param0} */
export async function getByIdApiReportsIdGet(
  // 叠加生成的Param类型 (非body参数swagger默认没有生成对象)
  params: API.getByIdApiReportsIdGetParams,
  options?: { [key: string]: any },
) {
  const { id: param0, ...queryParams } = params;
  return request<API.ReportModel>(`/api/reports/${param0}`, {
    method: 'GET',
    params: { ...queryParams },
    ...(options || {}),
  });
}
