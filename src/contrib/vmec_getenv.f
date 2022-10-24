      SUBROUTINE vmec_getenv(ename, evalue)
      IMPLICIT NONE
      CHARACTER(LEN=*) :: ename, evalue
c !DEC$ IF DEFINED (CRAY)
c       INTEGER :: lenname=0, lenval, ierror
c       CALL pxfgetenv(ename, lenname, evalue, lenval, ierror)
c !DEC$ ELSE
      CALL getenv(ename, evalue)
c !DEC$ ENDIF
      END SUBROUTINE vmec_getenv
