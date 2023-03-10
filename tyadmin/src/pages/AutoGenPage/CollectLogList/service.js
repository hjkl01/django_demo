import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryCollectLog(params) {
  return request('/api/xadmin/v1/collect_log', {
    params,
  });
}
export async function removeCollectLog(params) {
  return request(`/api/xadmin/v1/collect_log/${params}`, {
    method: 'DELETE',
  });
}
export async function addCollectLog(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/collect_log', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateCollectLog(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/collect_log/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryCollectLogVerboseName(params) {
  return request('/api/xadmin/v1/collect_log/verbose_name', {
    params,
  });
}
export async function queryCollectLogListDisplay(params) {
  return request('/api/xadmin/v1/collect_log/list_display', {
    params,
  });
}
export async function queryCollectLogDisplayOrder(params) {
  return request('/api/xadmin/v1/collect_log/display_order', {
    params,
  });
}


