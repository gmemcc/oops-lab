// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

/** Create POST /api/reports */
export async function createApiReportsPost(
  body: API.ReportModel,
  options?: { [key: string]: any },
) {
  return request<API.ReportModel>('/api/reports', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    data: body,
    ...(options || {}),
  });
}
