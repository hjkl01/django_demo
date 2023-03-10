import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryTyAdminSysLog(params) {
  return request('/api/xadmin/v1/ty_admin_sys_log', {
    params,
  });
}
export async function removeTyAdminSysLog(params) {
  return request(`/api/xadmin/v1/ty_admin_sys_log/${params}`, {
    method: 'DELETE',
  });
}
export async function addTyAdminSysLog(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/ty_admin_sys_log', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateTyAdminSysLog(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/ty_admin_sys_log/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryTyAdminSysLogVerboseName(params) {
  return request('/api/xadmin/v1/ty_admin_sys_log/verbose_name', {
    params,
  });
}
export async function queryTyAdminSysLogListDisplay(params) {
  return request('/api/xadmin/v1/ty_admin_sys_log/list_display', {
    params,
  });
}
export async function queryTyAdminSysLogDisplayOrder(params) {
  return request('/api/xadmin/v1/ty_admin_sys_log/display_order', {
    params,
  });
}


