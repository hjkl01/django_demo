import { DeleteOutlined, DownOutlined, EditOutlined, PlusOutlined, ExportOutlined } from '@ant-design/icons';
import { notification, Button, Col, Descriptions, Divider, Dropdown, Form, Input, Menu, message, Popconfirm, Popover, Row, Select, Tag, Transfer, Switch } from 'antd';
import React, { useEffect, useRef, useState } from 'react';
import KeyOutlined from '@ant-design/icons/lib/icons/KeyOutlined';
import { PageHeaderWrapper } from '@ant-design/pro-layout';
import ProTable from 'mtianyan-pro-table';
import CreateForm from './components/CreateForm';
import { addCollectLog, queryCollectLog, removeCollectLog, updateCollectLog, queryCollectLogVerboseName, queryCollectLogListDisplay, queryCollectLogDisplayOrder} from './service';
import UpdateForm from './components/UpdateForm';
import UploadAvatar from '@/components/UploadAvatar';


import moment from 'moment';
const { Option } = Select;
import { BooleanFormItem, dealManyToManyFieldTags, fileUpload, twoColumns, richForm, richCol, dealPureSelectField, orderForm, exportExcelCurrent, exportExcelAll, getUpdateColumns, dealRemoveError, dealError, BooleanDisplay, dealDateTimeDisplay, dealManyToManyField, dealTime, deepCopy, fieldErrorHandle, getTableColumns, renderManyToMany, richTrans, dealForeignKeyField, renderForeignKey, fieldsLevelErrorHandle } from '@/utils/utils';
import 'braft-editor/dist/index.css'
const FormItem = Form.Item;
const TableList = () => {
  const [createModalVisible, handleModalVisible] = useState(false);
  const [updateModalVisible, handleUpdateModalVisible] = useState(false);
 
  const [updateFormValues, setUpdateFormValues] = useState({});
  const actionRef = useRef();
  const addFormRef = useRef();
  const updateFormRef = useRef();

  const handleAdd = async fields => {
    const hide = message.loading('正在添加');

    try {
      await addCollectLog({ ...fields });
      hide();
      message.success('添加成功');
      return true;
    } catch (error) {
      return dealError(error, addFormRef, hide, "添加");
    }
  };

  const handleUpdate = async (value, current_id) => {
    const hide = message.loading('正在修改');

    try {
      await updateCollectLog(value, current_id);
      hide();
      message.success('修改成功');
      return true;
    } catch (error) {
      return dealError(error, updateFormRef, hide, "修改");
    }
  };

  const handleRemove = async selectedRows => {
    const hide = message.loading('正在删除');
    if (!selectedRows) return true;

    try {
      const ids = selectedRows.map(row => row.id).join(',');
      await removeCollectLog(ids);
      hide();
      message.success('删除成功');
      return true;
    } catch (error) {
      hide()
      return dealRemoveError(error, "删除");
    }
  };
 
  const dateFieldList = ["insert_time","created_time"]
  const base_columns = [{
                             title: 'id',
                             
        hideInForm: true,
        hideInSearch: true,
        
                             
                             dataIndex: 'id',
                             valueType: 'digit',
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: '主机',
                             
                             
                             dataIndex: 'hostname',
                             
                             rules: [
                                     {
                      required: true,
                      message: '主机为必填项',
                     },
                             ],
                             
                             
                        },
                      {
                             title: '运行时间/秒',
                             
                             
                             dataIndex: 'elapsed',
                             
                             rules: [
                                     {
                      required: true,
                      message: '运行时间/秒为必填项',
                     },
                             ],
                             
                             
                        },
                      {
                             title: '异常',
                             
                             
                             dataIndex: 'exception',
                             valueType: 'textarea',
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: '其他',
                             
                             
                             dataIndex: 'extra',
                             
                             rules: [
                                     {
                      required: true,
                      message: '其他为必填项',
                     },
                             ],
                             
                             
                        },
                      {
                             title: '文件',
                             
                             
                             dataIndex: 'fileinfo',
                             
                             rules: [
                                     {
                      required: true,
                      message: '文件为必填项',
                     },
                             ],
                             
                             
                        },
                      {
                             title: '函数名',
                             
                             
                             dataIndex: 'Function',
                             
                             rules: [
                                     {
                      required: true,
                      message: '函数名为必填项',
                     },
                             ],
                             
                             
                        },
                      {
                             title: '等级信息',
                             
                             
                             dataIndex: 'Level',
                             
                             rules: [
                                     {
                      required: true,
                      message: '等级信息为必填项',
                     },
                             ],
                             
                             
                        },
                      {
                             title: '行数',
                             
                             
                             dataIndex: 'line',
                             valueType: 'digit',
                             rules: [
                                     {
                      required: true,
                      message: '行数为必填项',
                     },
                             ],
                             
                             
                        },
                      {
                             title: '信息',
                             
                             
                             dataIndex: 'message',
                             valueType: 'textarea',
                             rules: [
                                     {
                      required: true,
                      message: '信息为必填项',
                     },
                             ],
                             
                             
                        },
                      {
                             title: '模块',
                             
                             
                             dataIndex: 'Module',
                             
                             rules: [
                                     {
                      required: true,
                      message: '模块为必填项',
                     },
                             ],
                             
                             
                        },
                      {
                             title: '名称',
                             
                             
                             dataIndex: 'name',
                             
                             rules: [
                                     {
                      required: true,
                      message: '名称为必填项',
                     },
                             ],
                             
                             
                        },
                      {
                             title: '进程信息',
                             
                             
                             dataIndex: 'Process',
                             valueType: 'digit',
                             rules: [
                                     {
                      required: true,
                      message: '进程信息为必填项',
                     },
                             ],
                             
                             
                        },
                      {
                             title: '线程信息',
                             
                             
                             dataIndex: 'Thread',
                             
                             rules: [
                                     {
                      required: true,
                      message: '线程信息为必填项',
                     },
                             ],
                             
                             
                        },
                      {
                             title: 'log打印时间',
                             
                             
                             dataIndex: 'insert_time',
                             valueType: 'dateTime',
                             rules: [
                                     {
                      required: true,
                      message: 'log打印时间为必填项',
                     },
                             ],
                             
                             
                        },
                      {
                             title: '创建时间',
                             
                             
                             dataIndex: 'created_time',
                             valueType: 'dateTime',
                             rules: [
                                     
                             ],
                             
                             
                        },
                          {
                              title: '操作',
                              dataIndex: 'option',
                              valueType: 'option',
                                    fixed: 'right',
          width: 100,
                              render: (text, record) => (
                                <>

                                  <EditOutlined title="编辑" className="icon" onClick={async () => {
                                   record.insert_time = record.insert_time === null ? record.insert_time : moment(record.insert_time);record.created_time = record.created_time === null ? record.created_time : moment(record.created_time);
                                    handleUpdateModalVisible(true);
                                    setUpdateFormValues(record);
                                  }} />
                                  <Divider type="vertical" />
                                  <Popconfirm
                                    title="您确定要删除log日志吗？"
                                    placement="topRight"
                                    onConfirm={() => {
                                      handleRemove([record])
                                      actionRef.current.reloadAndRest();
                                    }}
                                    okText="确定"
                                    cancelText="取消"
                                  >
                                    <DeleteOutlined title="删除" className="icon" />
                                  </Popconfirm>
                                </>
                              ),
                            },];

  let cp = deepCopy(base_columns);

  const [formOrder, setFormOrder] = useState([]);

  useEffect(() => {
    queryCollectLogDisplayOrder().then(r => {
      setFormOrder(r.form_order)
    })
  }, [])
  const table_columns = getTableColumns(cp);

  let order_cp = deepCopy(base_columns);
  const form_ordered = orderForm(formOrder, order_cp);

  const create_columns = [...form_ordered];
  const update_cp = deepCopy(form_ordered)
  const update_columns = getUpdateColumns(update_cp);

  const [columnsStateMap, setColumnsStateMap] = useState({});

  const [paramState, setParamState] = useState({});

  useEffect(() => {
    queryCollectLogListDisplay().then(value => {
      setColumnsStateMap(value)
    })
  }, [])


   

   
  return (
    <PageHeaderWrapper>
      <ProTable
        beforeSearchSubmit={(params => {
          dealTime(params, dateFieldList);
          return params;
        })}
        params={paramState}
        scroll={{ x: '100%' }}
        columnsStateMap={columnsStateMap}
        onColumnsStateChange={(map) => setColumnsStateMap(map)}
        headerTitle="log日志表格"
        actionRef={actionRef}
        rowKey="id"
        toolBarRender={(action, { selectedRows }) => [
          <Button type="primary" onClick={() => handleModalVisible(true)}>
            <PlusOutlined /> 新建
          </Button>,
          <Button type="primary" onClick={() => exportExcelAll(paramState, queryCollectLog, table_columns, 'log日志-All')}>
            <ExportOutlined /> 导出全部
          </Button>,
          <Input.Search style={{ marginRight: 20 }} placeholder="搜索log日志" onSearch={value => {
            setParamState({
              search: value,
            });
            actionRef.current.reload();
          }} />,
          selectedRows && selectedRows.length > 0 && (
            <Dropdown
              overlay={
                <Menu
                  onClick={async e => {
                    if (e.key === 'remove') {
                      await handleRemove(selectedRows);
                      actionRef.current.reloadAndRest();
                    }
                    else if (e.key === 'export_current') {
                      exportExcelCurrent(selectedRows, table_columns, 'log日志-select')
                    }
                  }}
                  selectedKeys={[]}
                >
                  <Menu.Item key="remove">批量删除</Menu.Item>
                  <Menu.Item key="export_current">导出已选</Menu.Item>
                </Menu>
              }
            >
              <Button>
                批量操作 <DownOutlined />
              </Button>
            </Dropdown>
          ),
        ]}
        tableAlertRender={({ selectedRowKeys, selectedRows }) => (
          selectedRowKeys.length > 0 ? <div>
            已选择{' '}
            <a
              style={{
                fontWeight: 600,
              }}
            >
              {selectedRowKeys.length}
            </a>{' '}
            项&nbsp;&nbsp;
          </div> : false

        )}
        request={(params, sorter, filter) => queryCollectLog({ ...params, sorter, filter })}
        columns={table_columns}
        rowSelection={{}}
      />
      <CreateForm onCancel={() => handleModalVisible(false)} modalVisible={createModalVisible}>
        <ProTable
          formRef={addFormRef}
          onSubmit={async value => {
            richTrans(value);
            const success = await handleAdd(value);

            if (success) {
              handleModalVisible(false);

              if (actionRef.current) {
                actionRef.current.reload();
              }
            }
          }}
          rowKey="key"
          type="form"
          search={twoColumns}
          form={
            {
              labelCol: { span: 6 },
              labelAlign: 'left',
            }}
          columns={create_columns}
          rowSelection={{}}
        />
      </CreateForm>
      <UpdateForm onCancel={() => handleUpdateModalVisible(false)} modalVisible={updateModalVisible}>
        <ProTable
          formRef={updateFormRef}
          onSubmit={async value => {
            richTrans(value);
            const success = await handleUpdate(value, updateFormValues.id);

            if (success) {
              handleUpdateModalVisible(false);

              if (actionRef.current) {
                actionRef.current.reload();
              }
            }
          }}
          rowKey="key"
          search={twoColumns}
          type="form"
          form={{
            initialValues: updateFormValues, labelCol: { span: 6 },
            labelAlign: 'left',
          }}
          columns={update_columns}
          rowSelection={{}}
        />
      </UpdateForm>
       
    </PageHeaderWrapper>
  );
};

export default TableList;
