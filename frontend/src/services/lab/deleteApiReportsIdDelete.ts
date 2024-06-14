// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

/** Delete DELETE /api/reports/${param0} */
export async function deleteApiReportsIdDelete(
  // 叠加生成的Param类型 (非body参数swagger默认没有生成对象)
  params: API.deleteApiReportsIdDeleteParams,
  options?: { [key: string]: any },
) {
  const { id: param0, ...queryParams } = params;
  return request<any>(`/api/reports/${param0}`, {
    method: 'DELETE',
    params: { ...queryParams },
    ...(options || {}),
  });
}
