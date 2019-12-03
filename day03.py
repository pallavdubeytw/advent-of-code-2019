def get_points(directions):
    points = [[0, 0]]
    points_index = 0

    for direction in directions:
        last_point = points[-1].copy()
        offset = int(direction[1:])

        if direction.startswith('R'):
            last_point[0] += offset
        elif direction.startswith('L'):
            last_point[0] -= offset
        elif direction.startswith('U'):
            last_point[1] += offset
        elif direction.startswith('D'):
            last_point[1] -= offset

        points.append(last_point)
        points_index += 1

    return points


wire_one = ['R991', 'U557', 'R554', 'U998', 'L861', 'D301', 'L891', 'U180', 'L280', 'D103', 'R828', 'D58', 'R373',
            'D278', 'L352', 'D583', 'L465', 'D301', 'R384', 'D638', 'L648', 'D413', 'L511', 'U596', 'L701', 'U463',
            'L664', 'U905', 'L374', 'D372', 'L269', 'U868', 'R494', 'U294', 'R661', 'U604', 'L629', 'U763', 'R771',
            'U96', 'R222', 'U227', 'L97', 'D793', 'L924', 'U781', 'L295', 'D427', 'R205', 'D387', 'L455', 'D904',
            'R254', 'D34', 'R341', 'U268', 'L344', 'D656', 'L715', 'U439', 'R158', 'U237', 'R199', 'U729', 'L428',
            'D125', 'R487', 'D506', 'R486', 'D496', 'R932', 'D918', 'R603', 'U836', 'R258', 'U15', 'L120', 'U528',
            'L102', 'D42', 'R385', 'U905', 'L472', 'D351', 'R506', 'U860', 'L331', 'D415', 'R963', 'D733', 'R108',
            'D527', 'L634', 'U502', 'L553', 'D623', 'R973', 'U209', 'L632', 'D588', 'R264', 'U553', 'L768', 'D689',
            'L708', 'D432', 'R247', 'U993', 'L146', 'U656', 'R710', 'U47', 'R783', 'U643', 'R954', 'U888', 'L84',
            'U202', 'R495', 'U66', 'R414', 'U993', 'R100', 'D557', 'L326', 'D645', 'R975', 'U266', 'R143', 'U730',
            'L491', 'D96', 'L161', 'U165', 'R97', 'D379', 'R930', 'D613', 'R178', 'D635', 'R192', 'U957', 'L450',
            'U149', 'R911', 'U220', 'L914', 'U659', 'L67', 'D825', 'L904', 'U137', 'L392', 'U333', 'L317', 'U310',
            'R298', 'D240', 'R646', 'U588', 'R746', 'U861', 'L958', 'D892', 'L200', 'U463', 'R246', 'D870', 'R687',
            'U815', 'R969', 'U864', 'L972', 'U254', 'L120', 'D418', 'L567', 'D128', 'R934', 'D217', 'R764', 'U128',
            'R146', 'U467', 'R690', 'U166', 'R996', 'D603', 'R144', 'D362', 'R885', 'D118', 'L882', 'U612', 'R270',
            'U917', 'L599', 'D66', 'L749', 'D498', 'L346', 'D920', 'L222', 'U439', 'R822', 'U891', 'R458', 'U15',
            'R831', 'U92', 'L164', 'D615', 'L439', 'U178', 'R409', 'D463', 'L452', 'U633', 'L683', 'U186', 'R402',
            'D609', 'L38', 'D699', 'L679', 'D74', 'R125', 'D145', 'R424', 'U961', 'L353', 'U43', 'R794', 'D519', 'L359',
            'D494', 'R812', 'D770', 'L657', 'U154', 'L137', 'U549', 'L193', 'D816', 'R333', 'U650', 'R49', 'D459',
            'R414', 'U72', 'R313', 'U231', 'R370', 'U680', 'L27', 'D221', 'L355', 'U342', 'L597', 'U748', 'R821',
            'D280', 'L307', 'U505', 'L160', 'U982', 'L527', 'D516', 'L245', 'U158', 'R565', 'D797', 'R99', 'D695',
            'L712', 'U155', 'L23', 'U964', 'L266', 'U623', 'L317', 'U445', 'R689', 'U150', 'L41', 'U536', 'R638',
            'D200', 'R763', 'D260', 'L234', 'U217', 'L881', 'D576', 'L223', 'U39', 'L808', 'D125', 'R950', 'U341',
            'L405']
wire_two = ['L993', 'D508', 'R356', 'U210', 'R42', 'D68', 'R827', 'D513', 'L564', 'D407', 'L945', 'U757', 'L517',
            'D253', 'R614', 'U824', 'R174', 'D536', 'R906', 'D291', 'R70', 'D295', 'R916', 'D754', 'L892', 'D736',
            'L528', 'D399', 'R76', 'D588', 'R12', 'U617', 'R173', 'D625', 'L533', 'D355', 'R178', 'D706', 'R139',
            'D419', 'R460', 'U976', 'L781', 'U973', 'L931', 'D254', 'R195', 'U42', 'R555', 'D151', 'R226', 'U713',
            'L755', 'U398', 'L933', 'U264', 'R352', 'U461', 'L472', 'D810', 'L257', 'U901', 'R429', 'U848', 'L181',
            'D362', 'R404', 'D234', 'L985', 'D392', 'R341', 'U608', 'L518', 'D59', 'L804', 'D219', 'L366', 'D28',
            'L238', 'D491', 'R265', 'U131', 'L727', 'D504', 'R122', 'U461', 'R732', 'D411', 'L910', 'D884', 'R954',
            'U341', 'L619', 'D949', 'L570', 'D823', 'R646', 'D226', 'R197', 'U892', 'L691', 'D294', 'L955', 'D303',
            'R490', 'D469', 'L503', 'D482', 'R390', 'D741', 'L715', 'D187', 'R378', 'U853', 'L70', 'D903', 'L589',
            'D481', 'L589', 'U911', 'R45', 'U348', 'R214', 'D10', 'R737', 'D305', 'R458', 'D291', 'R637', 'D721',
            'R440', 'U573', 'R442', 'D407', 'L63', 'U569', 'L903', 'D936', 'R518', 'U859', 'L370', 'D888', 'R498',
            'D759', 'R283', 'U469', 'R548', 'D185', 'R808', 'D81', 'L629', 'D761', 'R807', 'D878', 'R712', 'D183',
            'R382', 'D484', 'L791', 'D371', 'L188', 'D397', 'R645', 'U679', 'R415', 'D446', 'L695', 'U174', 'R707',
            'D36', 'R483', 'U877', 'L819', 'D538', 'L277', 'D2', 'R200', 'D838', 'R837', 'U347', 'L865', 'D945', 'R958',
            'U575', 'L924', 'D351', 'L881', 'U961', 'R899', 'U845', 'R816', 'U866', 'R203', 'D380', 'R766', 'D97',
            'R38', 'U148', 'L999', 'D332', 'R543', 'U10', 'R351', 'U281', 'L460', 'U309', 'L543', 'U795', 'L639',
            'D556', 'L882', 'D513', 'R722', 'U314', 'R531', 'D604', 'L418', 'U840', 'R864', 'D694', 'L530', 'U862',
            'R559', 'D639', 'R689', 'D201', 'L439', 'D697', 'R441', 'U175', 'R558', 'D585', 'R92', 'D191', 'L533',
            'D788', 'R154', 'D528', 'R341', 'D908', 'R811', 'U750', 'R172', 'D742', 'R113', 'U56', 'L517', 'D826',
            'L250', 'D269', 'L278', 'U74', 'R285', 'U904', 'L221', 'U270', 'R296', 'U671', 'L535', 'U340', 'L206',
            'U603', 'L852', 'D60', 'R648', 'D313', 'L282', 'D685', 'R482', 'U10', 'R829', 'U14', 'L12', 'U365', 'R996',
            'D10', 'R104', 'U654', 'R346', 'D458', 'R219', 'U247', 'L841', 'D731', 'R115', 'U400', 'L731', 'D904',
            'L487', 'U430', 'R612', 'U437', 'L865', 'D618', 'R747', 'U522', 'R309', 'U302', 'R9', 'U609', 'L201']

# wire_one = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
# wire_two = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']

# wire_one = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
# wire_two = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

# wire_one = ['R8', 'U5', 'L5', 'D3']
# wire_two = ['U7', 'R6', 'D4', 'L4']

# wire_one = ['R1002', 'U407', 'R530', 'D268', 'R516', 'U937', 'L74', 'U838', 'R784', 'D684', 'L912', 'U746', 'R189',
#             'U192', 'R868', 'D345', 'L972', 'D492', 'R942', 'U631', 'L559', 'U634', 'L80', 'U513', 'L746', 'D997',
#             'L348', 'D160', 'L655', 'U949', 'R717', 'U396', 'R549', 'D167', 'R591', 'U469', 'L22', 'U977', 'L167',
#             'D856', 'L320', 'D920', 'L396', 'U490', 'L895', 'U180', 'R661', 'D828', 'R864', 'U189', 'R307', 'U402',
#             'R409', 'U445', 'L101', 'D418', 'R812', 'U419', 'R319', 'U75', 'L813', 'D46', 'L491', 'U39', 'R737', 'U11',
#             'R177', 'U311', 'L278', 'U254', 'R475', 'U166', 'L515', 'D105', 'L694', 'D437', 'L298', 'U169', 'L613',
#             'D234', 'L999', 'U380', 'L711', 'D758', 'R932', 'D27', 'L951', 'D529', 'L935', 'D189', 'R816', 'D176',
#             'R98', 'D320', 'R965', 'D333', 'L367', 'U622', 'R18', 'U83', 'R275', 'D205', 'L960', 'U177', 'R750', 'D466',
#             'R442', 'U797', 'R355', 'D717', 'L569', 'D578', 'R384', 'U863', 'R541', 'U405', 'R527', 'D658', 'L514',
#             'U168', 'L64', 'D918', 'R947', 'D11', 'L189', 'D875', 'R599', 'U201', 'L165', 'U772', 'L679', 'U566',
#             'L195', 'U660', 'R896', 'D622', 'R678', 'U390', 'L984', 'D900', 'R889', 'D714', 'R557', 'U848', 'L176',
#             'U541', 'R518', 'D699', 'L904', 'D23', 'L55', 'D886', 'L206', 'D621', 'L48', 'D197', 'R502', 'D259', 'L779',
#             'D72', 'L183', 'U747', 'L424', 'U452', 'L603', 'U561', 'L430', 'D942', 'R515', 'D378', 'R962', 'U508',
#             'R230', 'D650', 'R804', 'D453', 'R899', 'D813', 'R484', 'U798', 'R456', 'D231', 'L316', 'U117', 'R630',
#             'D436', 'L985', 'D283', 'L393', 'D370', 'R158', 'U957', 'L914', 'D455', 'L875', 'U536', 'R889', 'U400',
#             'R347', 'U712', 'R487', 'D455', 'R428', 'U590', 'R127', 'D132', 'L202', 'U377', 'R138', 'U654', 'L760',
#             'D46', 'R213', 'D225', 'L817', 'U455', 'L612', 'U543', 'L525', 'U979', 'R591', 'D940', 'R446', 'U786',
#             'R750', 'U244', 'R325', 'U928', 'L44', 'U551', 'L955', 'U221', 'L986', 'U516', 'L916', 'D242', 'L280',
#             'D71', 'R80', 'U849', 'L271', 'U626', 'R737', 'D646', 'R82', 'U120', 'R646', 'U569', 'R463', 'D94', 'R570',
#             'U456', 'L548', 'D687', 'R221', 'D759', 'L606', 'D818', 'L859', 'U218', 'R682', 'U299', 'R818', 'D966',
#             'R407', 'U605', 'L859', 'D378', 'L53', 'D722', 'L216', 'D221', 'R639', 'U485', 'L865', 'D620', 'R99',
#             'D988', 'R944', 'D323', 'R540', 'U372', 'L470', 'U106', 'L804', 'D92', 'L177', 'U518', 'R277', 'U670',
#             'R451', 'D194', 'L695', 'D502', 'L601', 'U596', 'R374', 'U682', 'L19', 'D54', 'L156']
# wire_two = ['L1003', 'U22', 'R594', 'D241', 'L215', 'D906', 'R733', 'D831', 'L556', 'U421', 'L780', 'D242', 'R183',
#             'U311', 'R46', 'D52', 'R124', 'D950', 'L18', 'U985', 'R999', 'D528', 'R850', 'U575', 'L138', 'D62', 'L603',
#             'U467', 'R641', 'U155', 'L165', 'D63', 'L489', 'U4', 'R635', 'D460', 'L446', 'D938', 'R983', 'U494', 'L491',
#             'D433', 'L722', 'U427', 'L469', 'U832', 'L712', 'U798', 'R906', 'U804', 'R646', 'U721', 'R578', 'D194',
#             'L726', 'U803', 'L985', 'D934', 'R943', 'U198', 'R726', 'U341', 'R583', 'U998', 'L992', 'D401', 'L132',
#             'D681', 'L363', 'U949', 'L814', 'D977', 'R840', 'D145', 'L177', 'D291', 'L652', 'D396', 'R330', 'D951',
#             'L363', 'U813', 'R847', 'D374', 'R961', 'D912', 'R516', 'D178', 'R495', 'U49', 'R340', 'D395', 'R632',
#             'D991', 'R487', 'D263', 'R320', 'D948', 'R456', 'D142', 'L783', 'D888', 'R589', 'D999', 'L159', 'U686',
#             'R402', 'D586', 'L425', 'U946', 'R56', 'D979', 'L534', 'U313', 'R657', 'D401', 'L666', 'D504', 'R712',
#             'D232', 'L557', 'D620', 'R193', 'D670', 'L134', 'D975', 'R837', 'D901', 'R813', 'U459', 'L499', 'U450',
#             'L87', 'U84', 'L582', 'U310', 'R795', 'D280', 'L730', 'D458', 'L727', 'D196', 'R95', 'U210', 'R498', 'U760',
#             'R778', 'U325', 'R715', 'U479', 'R275', 'U557', 'L450', 'D196', 'L60', 'U115', 'R475', 'D265', 'L611',
#             'D372', 'R60', 'U935', 'L717', 'U809', 'L344', 'D854', 'L386', 'U473', 'R72', 'U968', 'L816', 'U900',
#             'R866', 'U172', 'R965', 'U383', 'R576', 'D774', 'R753', 'U788', 'L781', 'D237', 'L401', 'U786', 'R873',
#             'U331', 'R609', 'D232', 'L603', 'U685', 'L494', 'U177', 'L982', 'D173', 'L673', 'U772', 'L7', 'U7', 'R517',
#             'U573', 'R212', 'D413', 'L124', 'D810', 'L223', 'U137', 'L576', 'U95', 'R128', 'U896', 'L91', 'U932',
#             'L875', 'U917', 'R106', 'U911', 'L208', 'D507', 'L778', 'D59', 'L71', 'D352', 'R988', 'U708', 'L58', 'D429',
#             'L122', 'U771', 'L713', 'D801', 'R188', 'U661', 'R752', 'D374', 'R312', 'D848', 'L504', 'D540', 'R334',
#             'U517', 'R343', 'D739', 'L727', 'D552', 'L555', 'U580', 'L857', 'U474', 'R145', 'U188', 'L789', 'U698',
#             'R735', 'U131', 'L494', 'U162', 'L27', 'D849', 'L140', 'D849', 'R615', 'U798', 'R160', 'U492', 'R884',
#             'U521', 'L542', 'D729', 'R498', 'D853', 'R918', 'U565', 'R65', 'U32', 'L607', 'U552', 'L38', 'D822', 'L77',
#             'U490', 'L190', 'D93', 'L104', 'U268', 'R702', 'D112', 'L917', 'D876', 'L631', 'D139', 'L989', 'U810',
#             'R329', 'U253', 'L498', 'D767', 'L550', 'U666', 'L549', 'U616', 'R376']

wire_one_points = get_points(wire_one)
wire_two_points = get_points(wire_two)


# print(f'wire one pts: {wire_one_points}')
# print(f'wire two pts: {wire_two_points}')


def plot_increasing_x_points(current_pt, next_pt):
    pt_list = [current_pt, next_pt]
    pt_index = 0

    while pt_index < len(pt_list) and current_pt[0] < next_pt[0] - 1:
        pt_list.insert(pt_index + 1, [current_pt[0] + 1, current_pt[1]])
        pt_index += 1
        current_pt = pt_list[pt_index]

    return pt_list[1:-1]


def plot_decreasing_x_points(current_pt, next_pt):
    pt_list = [current_pt, next_pt]
    pt_index = 0

    while pt_index < len(pt_list) and current_pt[0] > next_pt[0] + 1:
        pt_list.insert(pt_index + 1, [current_pt[0] - 1, current_pt[1]])
        pt_index += 1
        current_pt = pt_list[pt_index]

    return pt_list[1:-1]


def plot_increasing_y_points(current_pt, next_pt):
    pt_list = [current_pt, next_pt]
    pt_index = 0

    while pt_index < len(pt_list) and current_pt[1] < next_pt[1] - 1:
        pt_list.insert(pt_index + 1, [current_pt[0], current_pt[1] + 1])
        pt_index += 1
        current_pt = pt_list[pt_index]

    return pt_list[1:-1]


def plot_decreasing_y_points(current_pt, next_pt):
    pt_list = [current_pt, next_pt]
    pt_index = 0

    while pt_index < len(pt_list) and current_pt[1] > next_pt[1] + 1:
        pt_list.insert(pt_index + 1, [current_pt[0], current_pt[1] - 1])
        pt_index += 1
        current_pt = pt_list[pt_index]

    return pt_list[1:-1]


def get_fill_axis(current_pt, next_pt):
    if current_pt[0] == next_pt[0]:
        return "y"
    else:
        return "x"


def is_increasing_fill(current_pt, next_pt, axis):
    if axis == 'x':
        if next_pt[0] > current_pt[0]:
            return True
        else:
            return False
    else:
        if next_pt[1] > current_pt[1]:
            return True
        else:
            return False


def plot_middle_points(points):
    points_copy = points.copy()
    pt_index = 0

    while pt_index < len(points_copy) - 1:
        axis = get_fill_axis(points_copy[pt_index], points_copy[pt_index + 1])
        increasing = is_increasing_fill(points_copy[pt_index], points_copy[pt_index + 1], axis)

        if axis == 'x' and increasing:
            to_insert = plot_increasing_x_points(points_copy[pt_index], points_copy[pt_index + 1])
            points_copy[pt_index + 1:pt_index + 1] = to_insert
            pt_index += len(to_insert) + 1

        elif axis == 'x' and not increasing:
            to_insert = plot_decreasing_x_points(points_copy[pt_index], points_copy[pt_index + 1])
            points_copy[pt_index + 1:pt_index + 1] = to_insert
            pt_index += len(to_insert) + 1

        elif axis == 'y' and increasing:
            to_insert = plot_increasing_y_points(points_copy[pt_index], points_copy[pt_index + 1])
            points_copy[pt_index + 1:pt_index + 1] = to_insert
            pt_index += len(to_insert) + 1

        elif axis == 'y' and not increasing:
            to_insert = plot_decreasing_y_points(points_copy[pt_index], points_copy[pt_index + 1])
            points_copy[pt_index + 1:pt_index + 1] = to_insert
            pt_index += len(to_insert) + 1

    return points_copy


all_pt_w_one = plot_middle_points(wire_one_points)
all_pt_w_two = plot_middle_points(wire_two_points)


# print(f'all points for one: {all_pt_w_one}')
# print(f'all points for one: {all_pt_w_two}')


def intersection(points_one, points_two):
    points_int = []

    for pt in points_one:
        if pt in points_two:
            points_int.append(pt)

    return points_int


# intersection_pts = intersection(all_pt_w_one, all_pt_w_two)

intersection_pts = [x for x in all_pt_w_one if x in all_pt_w_two]


# print(f'intersection: {intersection_pts}')


def distance_from_origin(point):
    return abs(point[0]) + abs(point[1])


def get_min_distance_point(points):
    distance_list = []
    for pt in points:
        distance_list.append(distance_from_origin(pt))
    return distance_list


print(f'min distance: {min(get_min_distance_point(intersection_pts)[1:])}')


def get_steps_for_each_intersection(points, intersection_points):
    steps_for_each_intersection = []
    for pt in intersection_points:
        steps_for_each_intersection.append(points.index(pt))
    return steps_for_each_intersection


steps_to_each_intersection_w_one = get_steps_for_each_intersection(all_pt_w_one, intersection_pts)
steps_to_each_intersection_w_two = get_steps_for_each_intersection(all_pt_w_two, intersection_pts)

# print(steps_to_each_intersection_w_one)
# print(steps_to_each_intersection_w_two)

steps_sum_list = []
index = 0
while index < len(steps_to_each_intersection_w_one):
    steps_sum_list.append(steps_to_each_intersection_w_one[index] + steps_to_each_intersection_w_two[index])
    index += 1

print(f'min steps: {min(steps_sum_list[1:])}')
