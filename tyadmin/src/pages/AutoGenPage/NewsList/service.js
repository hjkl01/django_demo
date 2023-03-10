import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryNews(params) {
  return request('/api/xadmin/v1/news', {
    params,
  });
}
export async function removeNews(params) {
  return request(`/api/xadmin/v1/news/${params}`, {
    method: 'DELETE',
  });
}
export async function addNews(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/news', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateNews(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/news/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryNewsVerboseName(params) {
  return request('/api/xadmin/v1/news/verbose_name', {
    params,
  });
}
export async function queryNewsListDisplay(params) {
  return request('/api/xadmin/v1/news/list_display', {
    params,
  });
}
export async function queryNewsDisplayOrder(params) {
  return request('/api/xadmin/v1/news/display_order', {
    params,
  });
}


