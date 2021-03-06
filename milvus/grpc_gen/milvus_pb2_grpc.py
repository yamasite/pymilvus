# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import milvus_pb2 as milvus__pb2
from . import status_pb2 as status__pb2


class MilvusServiceStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.CreateTable = channel.unary_unary(
            '/milvus.grpc.MilvusService/CreateTable',
            request_serializer=milvus__pb2.TableSchema.SerializeToString,
            response_deserializer=status__pb2.Status.FromString,
        )
        self.HasTable = channel.unary_unary(
            '/milvus.grpc.MilvusService/HasTable',
            request_serializer=milvus__pb2.TableName.SerializeToString,
            response_deserializer=milvus__pb2.BoolReply.FromString,
        )
        self.DescribeTable = channel.unary_unary(
            '/milvus.grpc.MilvusService/DescribeTable',
            request_serializer=milvus__pb2.TableName.SerializeToString,
            response_deserializer=milvus__pb2.TableSchema.FromString,
        )
        self.CountTable = channel.unary_unary(
            '/milvus.grpc.MilvusService/CountTable',
            request_serializer=milvus__pb2.TableName.SerializeToString,
            response_deserializer=milvus__pb2.TableRowCount.FromString,
        )
        self.ShowTables = channel.unary_unary(
            '/milvus.grpc.MilvusService/ShowTables',
            request_serializer=milvus__pb2.Command.SerializeToString,
            response_deserializer=milvus__pb2.TableNameList.FromString,
        )
        self.ShowTableInfo = channel.unary_unary(
            '/milvus.grpc.MilvusService/ShowTableInfo',
            request_serializer=milvus__pb2.TableName.SerializeToString,
            response_deserializer=milvus__pb2.TableInfo.FromString,
        )
        self.DropTable = channel.unary_unary(
            '/milvus.grpc.MilvusService/DropTable',
            request_serializer=milvus__pb2.TableName.SerializeToString,
            response_deserializer=status__pb2.Status.FromString,
        )
        self.CreateIndex = channel.unary_unary(
            '/milvus.grpc.MilvusService/CreateIndex',
            request_serializer=milvus__pb2.IndexParam.SerializeToString,
            response_deserializer=status__pb2.Status.FromString,
        )
        self.DescribeIndex = channel.unary_unary(
            '/milvus.grpc.MilvusService/DescribeIndex',
            request_serializer=milvus__pb2.TableName.SerializeToString,
            response_deserializer=milvus__pb2.IndexParam.FromString,
        )
        self.DropIndex = channel.unary_unary(
            '/milvus.grpc.MilvusService/DropIndex',
            request_serializer=milvus__pb2.TableName.SerializeToString,
            response_deserializer=status__pb2.Status.FromString,
        )
        self.CreatePartition = channel.unary_unary(
            '/milvus.grpc.MilvusService/CreatePartition',
            request_serializer=milvus__pb2.PartitionParam.SerializeToString,
            response_deserializer=status__pb2.Status.FromString,
        )
        self.ShowPartitions = channel.unary_unary(
            '/milvus.grpc.MilvusService/ShowPartitions',
            request_serializer=milvus__pb2.TableName.SerializeToString,
            response_deserializer=milvus__pb2.PartitionList.FromString,
        )
        self.DropPartition = channel.unary_unary(
            '/milvus.grpc.MilvusService/DropPartition',
            request_serializer=milvus__pb2.PartitionParam.SerializeToString,
            response_deserializer=status__pb2.Status.FromString,
        )
        self.Insert = channel.unary_unary(
            '/milvus.grpc.MilvusService/Insert',
            request_serializer=milvus__pb2.InsertParam.SerializeToString,
            response_deserializer=milvus__pb2.VectorIds.FromString,
        )
        self.GetVectorByID = channel.unary_unary(
            '/milvus.grpc.MilvusService/GetVectorByID',
            request_serializer=milvus__pb2.VectorIdentity.SerializeToString,
            response_deserializer=milvus__pb2.VectorData.FromString,
        )
        self.GetVectorIDs = channel.unary_unary(
            '/milvus.grpc.MilvusService/GetVectorIDs',
            request_serializer=milvus__pb2.GetVectorIDsParam.SerializeToString,
            response_deserializer=milvus__pb2.VectorIds.FromString,
        )
        self.Search = channel.unary_unary(
            '/milvus.grpc.MilvusService/Search',
            request_serializer=milvus__pb2.SearchParam.SerializeToString,
            response_deserializer=milvus__pb2.TopKQueryResult.FromString,
        )
        self.SearchByID = channel.unary_unary(
            '/milvus.grpc.MilvusService/SearchByID',
            request_serializer=milvus__pb2.SearchByIDParam.SerializeToString,
            response_deserializer=milvus__pb2.TopKQueryResult.FromString,
        )
        self.SearchInFiles = channel.unary_unary(
            '/milvus.grpc.MilvusService/SearchInFiles',
            request_serializer=milvus__pb2.SearchInFilesParam.SerializeToString,
            response_deserializer=milvus__pb2.TopKQueryResult.FromString,
        )
        self.Cmd = channel.unary_unary(
            '/milvus.grpc.MilvusService/Cmd',
            request_serializer=milvus__pb2.Command.SerializeToString,
            response_deserializer=milvus__pb2.StringReply.FromString,
        )
        self.DeleteByID = channel.unary_unary(
            '/milvus.grpc.MilvusService/DeleteByID',
            request_serializer=milvus__pb2.DeleteByIDParam.SerializeToString,
            response_deserializer=status__pb2.Status.FromString,
        )
        self.PreloadTable = channel.unary_unary(
            '/milvus.grpc.MilvusService/PreloadTable',
            request_serializer=milvus__pb2.TableName.SerializeToString,
            response_deserializer=status__pb2.Status.FromString,
        )
        self.Flush = channel.unary_unary(
            '/milvus.grpc.MilvusService/Flush',
            request_serializer=milvus__pb2.FlushParam.SerializeToString,
            response_deserializer=status__pb2.Status.FromString,
        )
        self.Compact = channel.unary_unary(
            '/milvus.grpc.MilvusService/Compact',
            request_serializer=milvus__pb2.TableName.SerializeToString,
            response_deserializer=status__pb2.Status.FromString,
        )


class MilvusServiceServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def CreateTable(self, request, context):
        """*
        @brief This method is used to create table

        @param TableSchema, use to provide table information to be created.

        @return Status
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HasTable(self, request, context):
        """*
        @brief This method is used to test table existence.

        @param TableName, table name is going to be tested.

        @return BoolReply
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeTable(self, request, context):
        """*
        @brief This method is used to get table schema.

        @param TableName, target table name.

        @return TableSchema
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CountTable(self, request, context):
        """*
        @brief This method is used to get table schema.

        @param TableName, target table name.

        @return TableRowCount
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ShowTables(self, request, context):
        """*
        @brief This method is used to list all tables.

        @param Command, dummy parameter.

        @return TableNameList
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ShowTableInfo(self, request, context):
        """*
        @brief This method is used to get table detail information.

        @param TableName, target table name.

        @return TableInfo
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DropTable(self, request, context):
        """*
        @brief This method is used to delete table.

        @param TableName, table name is going to be deleted.

        @return TableNameList
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateIndex(self, request, context):
        """*
        @brief This method is used to build index by table in sync mode.

        @param IndexParam, index paramters.

        @return Status
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeIndex(self, request, context):
        """*
        @brief This method is used to describe index

        @param TableName, target table name.

        @return IndexParam
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DropIndex(self, request, context):
        """*
        @brief This method is used to drop index

        @param TableName, target table name.

        @return Status
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreatePartition(self, request, context):
        """*
        @brief This method is used to create partition

        @param PartitionParam, partition parameters.

        @return Status
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ShowPartitions(self, request, context):
        """*
        @brief This method is used to show partition information

        @param TableName, target table name.

        @return PartitionList
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DropPartition(self, request, context):
        """*
        @brief This method is used to drop partition

        @param PartitionParam, target partition.

        @return Status
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Insert(self, request, context):
        """*
        @brief This method is used to add vector array to table.

        @param InsertParam, insert parameters.

        @return VectorIds
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVectorByID(self, request, context):
        """*
        @brief This method is used to get vector data by id.

        @param VectorIdentity, target vector id.

        @return VectorData
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVectorIDs(self, request, context):
        """*
        @brief This method is used to get vector ids from a segment

        @param GetVectorIDsParam, target table and segment

        @return VectorIds
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Search(self, request, context):
        """*
        @brief This method is used to query vector in table.

        @param SearchParam, search parameters.

        @return TopKQueryResult
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchByID(self, request, context):
        """*
        @brief This method is used to query vector by id.

        @param SearchByIDParam, search parameters.

        @return TopKQueryResult
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchInFiles(self, request, context):
        """*
        @brief This method is used to query vector in specified files.

        @param SearchInFilesParam, search in files paremeters.

        @return TopKQueryResult
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Cmd(self, request, context):
        """*
        @brief This method is used to give the server status.

        @param Command, command string

        @return StringReply
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteByID(self, request, context):
        """*
        @brief This method is used to delete vector by id

        @param DeleteByIDParam, delete parameters.

        @return status
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PreloadTable(self, request, context):
        """*
        @brief This method is used to preload table

        @param TableName, target table name.

        @return Status
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Flush(self, request, context):
        """*
        @brief This method is used to flush buffer into storage.

        @param FlushParam, flush parameters

        @return Status
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Compact(self, request, context):
        """*
        @brief This method is used to compact table

        @param TableName, target table name.

        @return Status
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MilvusServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'CreateTable': grpc.unary_unary_rpc_method_handler(
            servicer.CreateTable,
            request_deserializer=milvus__pb2.TableSchema.FromString,
            response_serializer=status__pb2.Status.SerializeToString,
        ),
        'HasTable': grpc.unary_unary_rpc_method_handler(
            servicer.HasTable,
            request_deserializer=milvus__pb2.TableName.FromString,
            response_serializer=milvus__pb2.BoolReply.SerializeToString,
        ),
        'DescribeTable': grpc.unary_unary_rpc_method_handler(
            servicer.DescribeTable,
            request_deserializer=milvus__pb2.TableName.FromString,
            response_serializer=milvus__pb2.TableSchema.SerializeToString,
        ),
        'CountTable': grpc.unary_unary_rpc_method_handler(
            servicer.CountTable,
            request_deserializer=milvus__pb2.TableName.FromString,
            response_serializer=milvus__pb2.TableRowCount.SerializeToString,
        ),
        'ShowTables': grpc.unary_unary_rpc_method_handler(
            servicer.ShowTables,
            request_deserializer=milvus__pb2.Command.FromString,
            response_serializer=milvus__pb2.TableNameList.SerializeToString,
        ),
        'ShowTableInfo': grpc.unary_unary_rpc_method_handler(
            servicer.ShowTableInfo,
            request_deserializer=milvus__pb2.TableName.FromString,
            response_serializer=milvus__pb2.TableInfo.SerializeToString,
        ),
        'DropTable': grpc.unary_unary_rpc_method_handler(
            servicer.DropTable,
            request_deserializer=milvus__pb2.TableName.FromString,
            response_serializer=status__pb2.Status.SerializeToString,
        ),
        'CreateIndex': grpc.unary_unary_rpc_method_handler(
            servicer.CreateIndex,
            request_deserializer=milvus__pb2.IndexParam.FromString,
            response_serializer=status__pb2.Status.SerializeToString,
        ),
        'DescribeIndex': grpc.unary_unary_rpc_method_handler(
            servicer.DescribeIndex,
            request_deserializer=milvus__pb2.TableName.FromString,
            response_serializer=milvus__pb2.IndexParam.SerializeToString,
        ),
        'DropIndex': grpc.unary_unary_rpc_method_handler(
            servicer.DropIndex,
            request_deserializer=milvus__pb2.TableName.FromString,
            response_serializer=status__pb2.Status.SerializeToString,
        ),
        'CreatePartition': grpc.unary_unary_rpc_method_handler(
            servicer.CreatePartition,
            request_deserializer=milvus__pb2.PartitionParam.FromString,
            response_serializer=status__pb2.Status.SerializeToString,
        ),
        'ShowPartitions': grpc.unary_unary_rpc_method_handler(
            servicer.ShowPartitions,
            request_deserializer=milvus__pb2.TableName.FromString,
            response_serializer=milvus__pb2.PartitionList.SerializeToString,
        ),
        'DropPartition': grpc.unary_unary_rpc_method_handler(
            servicer.DropPartition,
            request_deserializer=milvus__pb2.PartitionParam.FromString,
            response_serializer=status__pb2.Status.SerializeToString,
        ),
        'Insert': grpc.unary_unary_rpc_method_handler(
            servicer.Insert,
            request_deserializer=milvus__pb2.InsertParam.FromString,
            response_serializer=milvus__pb2.VectorIds.SerializeToString,
        ),
        'GetVectorByID': grpc.unary_unary_rpc_method_handler(
            servicer.GetVectorByID,
            request_deserializer=milvus__pb2.VectorIdentity.FromString,
            response_serializer=milvus__pb2.VectorData.SerializeToString,
        ),
        'GetVectorIDs': grpc.unary_unary_rpc_method_handler(
            servicer.GetVectorIDs,
            request_deserializer=milvus__pb2.GetVectorIDsParam.FromString,
            response_serializer=milvus__pb2.VectorIds.SerializeToString,
        ),
        'Search': grpc.unary_unary_rpc_method_handler(
            servicer.Search,
            request_deserializer=milvus__pb2.SearchParam.FromString,
            response_serializer=milvus__pb2.TopKQueryResult.SerializeToString,
        ),
        'SearchByID': grpc.unary_unary_rpc_method_handler(
            servicer.SearchByID,
            request_deserializer=milvus__pb2.SearchByIDParam.FromString,
            response_serializer=milvus__pb2.TopKQueryResult.SerializeToString,
        ),
        'SearchInFiles': grpc.unary_unary_rpc_method_handler(
            servicer.SearchInFiles,
            request_deserializer=milvus__pb2.SearchInFilesParam.FromString,
            response_serializer=milvus__pb2.TopKQueryResult.SerializeToString,
        ),
        'Cmd': grpc.unary_unary_rpc_method_handler(
            servicer.Cmd,
            request_deserializer=milvus__pb2.Command.FromString,
            response_serializer=milvus__pb2.StringReply.SerializeToString,
        ),
        'DeleteByID': grpc.unary_unary_rpc_method_handler(
            servicer.DeleteByID,
            request_deserializer=milvus__pb2.DeleteByIDParam.FromString,
            response_serializer=status__pb2.Status.SerializeToString,
        ),
        'PreloadTable': grpc.unary_unary_rpc_method_handler(
            servicer.PreloadTable,
            request_deserializer=milvus__pb2.TableName.FromString,
            response_serializer=status__pb2.Status.SerializeToString,
        ),
        'Flush': grpc.unary_unary_rpc_method_handler(
            servicer.Flush,
            request_deserializer=milvus__pb2.FlushParam.FromString,
            response_serializer=status__pb2.Status.SerializeToString,
        ),
        'Compact': grpc.unary_unary_rpc_method_handler(
            servicer.Compact,
            request_deserializer=milvus__pb2.TableName.FromString,
            response_serializer=status__pb2.Status.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'milvus.grpc.MilvusService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
